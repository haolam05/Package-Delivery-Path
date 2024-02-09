from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ShippingForm(FlaskForm):
  sender_name = StringField(
    "Sender's Name",
    validators = [DataRequired()]
  )

  recipient_name = StringField(
    "Recipient's Name",
    validators = [DataRequired()]
  )

  origin = SelectField(
    "Origin",
    validators=[DataRequired()],
    coerce = str
  )

  destination = SelectField(
    "Destination",
    validators=[DataRequired()],
    coerce = str
  )

  has_express = BooleanField("Express")

  submit = SubmitField("Submit")
