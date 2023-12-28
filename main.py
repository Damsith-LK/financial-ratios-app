from flask import Flask, render_template, redirect, flash
from flask_bootstrap import Bootstrap5
import datetime
from ratios import ratios_dict
from forms import FinancialRatiosForm, SignupForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, UserMixin, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
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

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, user_id)


# CONFIGURE TABLES
class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()


year = datetime.datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", year=year, is_logged_in=current_user.is_authenticated)

@app.route("/ratio/<string:ratio>", methods=["GET", "POST"])
def ratio(ratio):
    is_post = False
    result = None
    form = FinancialRatiosForm()
    # In order to check if the ratio in url actually exists:
    if ratio in ratios_dict:
        name = ratios_dict[ratio]["name"]
        description = ratios_dict[ratio]["description"]
        # Below line will fetch a list of 2 items from ratio.py
        labels = ratios_dict[ratio]["labels"]
        # Upon form submit the following lines of code will get triggered
        if form.validate_on_submit():
            input_1 = form.input_1.data
            input_2 = form.input_2.data
            # Calling the function stored inside dict
            result = ratios_dict[ratio]["function"](input_1, input_2)
            is_post = True

    return render_template("ratio.html", ratio=ratio, ratio_name=name, ratio_description=description, form=form, labels=labels, year=year, is_post=is_post, result=result, is_logged_in=current_user.is_authenticated)

@app.route("/all-ratios")
def all_ratios():
    return render_template("all_ratios.html", ratios_dict=ratios_dict, is_logged_in=current_user.is_authenticated)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data.lower()
        password = form.password.data
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
    form = LoginForm()

    return render_template("login.html", form=form, year=year, is_logged_in=current_user.is_authenticated)

if __name__ == "__main__":
    app.run(debug=True, port=5002)