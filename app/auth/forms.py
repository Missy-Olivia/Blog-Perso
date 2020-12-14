from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from ..models import User

class RegForm(FlaskForm):
    email = StringField('Enter Email Address',validators=[Required(),Email()])
    username = StringField('Enter Username',validators = [Required()])
    password = PasswordField('Enter Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email exists already!')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username exists already!')

class loginForm(FlaskForm):
    email = StringField('Enter Email Address',validators=[Required(),Email()])
    password = PasswordField('Enter Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
