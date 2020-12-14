from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from ..models import Mail_list

class blogForm(FlaskForm):

 title = StringField('Blog Title',validators=[Required()])
 content = TextAreaField('Blog Content')
 image = FileField('Featured Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
 submit = SubmitField('Submit')
 

class commentForm(FlaskForm):

 comment = TextAreaField('Comment', validators=[Required()])

 submit = SubmitField('Submit')

class updateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class subscribeForm(FlaskForm):
    email = StringField('Email Address',validators=[Required(),Email()])
    name = StringField('Name',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if Mail_list.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email already exists in mail list!')
