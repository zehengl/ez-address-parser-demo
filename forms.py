from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")
