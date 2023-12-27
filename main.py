from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import datetime
from ratios import ratios_dict
from forms import FinancialRatiosForm
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
Bootstrap5(app)
# Initialize a secret key here
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
db = SQLAlchemy()
db.init_app(app)

# CONFIGURE TABLES
class Users(db.Model):
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
    return render_template("index.html", year=year)

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

    return render_template("ratio.html", ratio=ratio, ratio_name=name, ratio_description=description, form=form, labels=labels, year=year, is_post=is_post, result=result)

@app.route("/all-ratios")
def all_ratios():
    return render_template("all_ratios.html", ratios_dict=ratios_dict)

@app.route("/signup")
def signup():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5002)