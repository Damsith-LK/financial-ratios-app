# Import this on main.py. Contains the common form for calculations

from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class FinancialRatiosForm(FlaskForm):
    input_1 = FloatField(validators=[DataRequired()])
    input_2 = FloatField(validators=[DataRequired()])
    submit = SubmitField("Calculate")

class SignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign me up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let me in!")

class SaveToHistory(FlaskForm):
    note = StringField("Notes (Optional)")
    submit = SubmitField("Save to history")