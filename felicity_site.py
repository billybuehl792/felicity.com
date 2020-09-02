#!python3
# felicity_site.py - felicity gunn website

from flask import Flask, flash, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, \
                        logout_user, current_user, login_required

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'fbcaaa74745faa81274628eabbaffeda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# db objects
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'User("{self.username}", "{self.email}")'


class Piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    piece_name = db.Column(db.String(20), nullable=False)
    piece_descr = db.Column(db.Text, nullable=False)
    piece_img = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Piece("{self.piece_name}")'


# forms
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
        user = User.query.filter_by(username=form.user.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('customize'))

        flash('Username or password incorrect', 'message')

    return render_template('login.html', title='Login', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'message')
    return redirect(url_for('login'))


@app.route('/customize', methods=['GET', 'POST'])
@login_required
def customize():
    return 'Customize'


if __name__ == '__main__':
    app.run(debug=True)
