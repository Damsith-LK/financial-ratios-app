from flask import Flask, render_template, redirect, flash, url_for, session
from flask_bootstrap import Bootstrap5
import datetime
from ratios import ratios_dict
from forms import FinancialRatiosForm, SignupForm, LoginForm, SaveToHistory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, UserMixin, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import relationship
import os

SALT_LENGTH = 8
app = Flask(__name__)
Bootstrap5(app)
# Initialize a secret key here
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
db = SQLAlchemy()
db.init_app(app)

# CONFIGURE FLASK-LOGIN
login_manager = LoginManager()
login_manager.init_app(app)

def check_notes(notes: str) -> None or str:
    """For checking if notes have a value like 'nothing' or 'None'. If so, returns None.
    Use this in ratio()"""
    ignore_list = ["none", "nothing", "no", ".", "n", "ignore", "false", "null", "no notes", "something", "type"]
    if notes.lower() in ignore_list:
        return None
    return notes

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, user_id)

# CONFIGURE TABLES
# Have to use one-to-many relationship between Users and Calculations. One user can have many saved calculations.
class Users(UserMixin, db.Model):
    """Parent table containing data about users of the website"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    calculations = relationship("Calculations", back_populates="user")

class Calculations(db.Model):
    """Child table containing calculations done by users and relevant information"""
    __tablename__ = "calculations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("Users", back_populates="calculations")
    calculation_name = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)
    input_1_name = db.Column(db.String, nullable=False)
    input_1_val = db.Column(db.Float, nullable=False)
    input_2_name = db.Column(db.String, nullable=False)
    input_2_val = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


year = datetime.datetime.now().year

@app.route("/")
def home():
    display_cals = None
    # Getting the saved calculations of the current user
    if current_user.is_authenticated:
        all_cals = db.session.execute(db.select(Calculations).where(Calculations.user_id == current_user.id)).scalars().all()
        # Get only the 5 most recent calculations if there are 5 or more calculations
        if len(all_cals) >= 5:
            display_cals = all_cals[-5:]
        else:
            display_cals = all_cals
    return render_template("index.html", year=year, is_logged_in=current_user.is_authenticated, display_cals=display_cals)

@app.route("/ratio/<string:ratio>", methods=["GET", "POST"])
def ratio(ratio):
    result = None
    is_post = False
    form = FinancialRatiosForm()
    form_2 = SaveToHistory()
    # In order to check if the ratio in url actually exists:
    if ratio in ratios_dict:
        name = ratios_dict[ratio]["name"]
        description = ratios_dict[ratio]["description"]
        # Below line will fetch a list of 2 items from ratio.py
        labels = ratios_dict[ratio]["labels"]
        # Upon form submit the following lines of code will get triggered
        if form.validate_on_submit():
            print("f1")
            session['input_1'] = form.input_1.data
            session['input_2'] = form.input_2.data
            # Calling the function stored inside dict
            result = ratios_dict[ratio]["function"](session['input_1'], session['input_2'])
            session['result'] = result
            is_post = True
        if form_2.validate_on_submit() and form_2.submit.data:
            print("f2")
            date = datetime.datetime.now().strftime("%d, %b %Y")
            notes = form_2.note.data
            # Creating new record in DB
            new_calculation = Calculations(
                user=current_user,
                calculation_name=name,
                result=session['result'],
                input_1_name=labels[0],
                input_1_val=session['input_1'],
                input_2_name=labels[1],
                input_2_val=session['input_2'],
                notes=check_notes(notes),
                date=date
            )
            db.session.add(new_calculation)
            db.session.commit()

    return render_template("ratio.html", ratio=ratio, ratio_name=name, ratio_description=description, form=form, form_2=form_2,
                           labels=labels, year=year, is_post=is_post, result=result, is_logged_in=current_user.is_authenticated)

@app.route("/all-ratios")
def all_ratios():
    return render_template("all_ratios.html", ratios_dict=ratios_dict, is_logged_in=current_user.is_authenticated)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Create a new user account"""
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data.lower()
        password = form.password.data
        # Check if the email already exists in the DB
        check_email = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
        if check_email:
            flash("You've already signed up with that email. Log in instead.", category="error")
            return redirect(url_for("login"))
        ## If the email doesn't exist in DB, following code will be executed and a new user account will be created
        # Hash the password
        hashed_password = generate_password_hash(password=password, salt_length=SALT_LENGTH)
        # Create a new user
        new_user = Users(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        # Authenticate the user with flask-login
        login_user(new_user)
        return redirect("/")

    return render_template("signup.html", year=year, form=form, is_logged_in=current_user.is_authenticated)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in to an existing user account"""
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        # Search for email in the DB
        search_email = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
        # If email doesn't exist in DB
        if not search_email:
            flash("Sorry, that email doesn't exist. You'll have to sign up with it.", category="error")
            return redirect(url_for("signup"))
        # If password is incorrect
        elif not check_password_hash(search_email.password, password):
            flash("The password you entered is incorrect.")
            return redirect(url_for("login"))
        ## If everything is alright, following code will be executed and the user will be logged in
        login_user(search_email, remember=True)
        return redirect("/")

    return render_template("login.html", form=form, year=year, is_logged_in=current_user.is_authenticated)

@app.route("/saved-calculations")
def saved_calculations():
    """Page for displaying all the calculations saved by the user"""
    if not current_user.is_authenticated:
        flash("You need to have an account in order to save calculations and view them, dummy.")
        return redirect(url_for("signup"))
    return render_template("saved_calculations", year=year, is_logged_in=current_user.is_authenticated)

@app.route("/logout")
def logout():
    """Logs out an existing user"""
    if current_user.is_authenticated:
        logout_user()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5002)
