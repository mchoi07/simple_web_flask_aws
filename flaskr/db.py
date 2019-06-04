
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://jeremie.havice:Jeremie.havice@techfield-0430.c48wltpqrvjo.us-east-2.rds.amazonaws.com:3306/techfield0430'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    weight = db.Column(db.Decimal, unique=False, nullable=False)
    height = db.Column(db.Decimal, unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.lastname


