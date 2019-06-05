from sqlalchemy import create_engine, MetaData, Table
import click
from flask import current_app, g
from flask.cli import with_appcontext
"""
engine = create_engine('mysql+pymysql://Admin:techfieldbddb@techfield-0430.c48wltpqrvjo.us-east-2.rds.amazonaws.com:3306/testDB', convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('info', metadata, autoload=True)
con = engine.connect()
con.execute(users.insert(), firstname='Hello', lastname="goodbye", weight="135", height="5'7", age="138")
"""

def get_db():
    if 'db' not in g:
        g.db = create_engine(
            'mysql+pymysql://Admin:techfieldbddb@techfield-0430.c48wltpqrvjo.us-east-2.rds.amazonaws.com:3306/testDB',
            convert_unicode=True)
        metadata = MetaData(bind=g.db)
        g.db.table = Table('info', metadata, autoload=True)

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)