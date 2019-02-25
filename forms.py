import os
from flask import Flask
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired 
from wtforms import StringField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LogIn(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    
class UploadPhoto(FlaskForm):
    imagefile = FileField('Photo',validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])
    description = StringField('Description', validators=[DataRequired()])
