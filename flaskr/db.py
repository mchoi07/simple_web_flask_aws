import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    weight = db.Column(db.Decimal, unique=False, nullable=False)
    height = db.Column(db.Decimal, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.lastname


