# Import this on main.py. Contains the common form for calculations

from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class FinancialRatiosForm(FlaskForm):
    input_1 = FloatField(validators=[DataRequired()])
    input_2 = FloatField(validators=[DataRequired()])
    submit = SubmitField("Calculate")