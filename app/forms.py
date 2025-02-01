from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(Form):
	"""Class for login form."""

	user = TextField('user', validators=[DataRequired()])
	password = TextField('password', validators=[DataRequired()])