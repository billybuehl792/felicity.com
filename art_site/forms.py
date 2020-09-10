# forms.py - frontend web forms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, \
                    FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')


class UploadForm(FlaskForm):
    title = StringField('Piece Title', validators=[DataRequired()])
    date = StringField('Piece Date', validators=[DataRequired()])
    descr = TextAreaField('Piece Description', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit Piece')
