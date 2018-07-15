from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
