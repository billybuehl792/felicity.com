# models.py - database structure

from art_site import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'User("{self.username}", "{self.email}")'


class Sketch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    descr = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Sketch("{self.title}")'


class ArtPiece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    descr = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'ArtPiece("{self.title}")'
