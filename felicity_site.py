#!python3
# felicity_site.py - felicity gunn website

from flask import Flask, render_template, url_for

app = Flask(__name__)

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
