from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):
    address = TextField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")
