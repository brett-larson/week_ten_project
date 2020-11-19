"""
    Author: Brett Larson
    Date: 11/04/2020

    Description:
        This Python file creates Flask forms in combination with HTML files located in the
        templates folder.
"""

# Required Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired


class PaymentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    card_number = StringField("Credit Card Number", validators=[DataRequired()])
    exp_date = StringField("Expiration Date", validators=[DataRequired()])
    zip_code = StringField("Zip Code", validators=[DataRequired()])
    purchase_amt = DecimalField("Purchase Amount", validators=[DataRequired()])
    submit = SubmitField("Submit")
