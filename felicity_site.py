#!python3
# felicity_site.py - felicity gunn website

from flask import Flask, flash, render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fbcaaa74745faa81274628eabbaffeda'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'User("{self.username}", "{self.email}")'


class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/artwork')
def artwork():
    return render_template('artwork.html', title='Artwork')

@app.route('/sketchbook')
def sketchbook():
    return render_template('sketchbook.html', title='Sketchbook')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form)
        if form.user.data == 'felice' and form.password.data == 'pass':
            return redirect(url_for('home'))
        else:
            flash('Email or password incorrect', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
