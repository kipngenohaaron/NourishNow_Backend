from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,unique=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    donations = db.relationship('Donation', backref='user', lazy=True)
    articles = db.relationship('Article', backref='user', lazy=True)




class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type = db.Column(db.String)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.Column(db.String)
    title = db.Column(db.String)
    body = db.Column(db.Text)
