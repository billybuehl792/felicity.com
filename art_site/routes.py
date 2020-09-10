#!python3
# felicity_site.py - felicity gunn website

from flask import flash, url_for, redirect, render_template, request
from art_site import app, db
from art_site.forms import LoginForm, UploadForm
from art_site.models import User, Sketch, ArtPiece
from flask_login import login_user

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


if __name__ == '__main__':
    app.run(debug=True)
