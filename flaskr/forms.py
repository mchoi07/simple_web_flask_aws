import functools
from flaskr.database import get_db
from sqlalchemy import create_engine, MetaData, Table
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

#from flaskr.db import get_db

bp = Blueprint('forms', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        weight = request.form['weight']
        height = request.form['height']
        age = request.form['age']
        error = None

        if not firstname:
            error = 'First name is required.'
        if not lastname:
            error = 'Last name is required'
        if error is not None:
            flash(error)
        else:
            """
            db = get_db()
            db.execute(
                'INSERT INTO info (firstname, lastname, weight, height, age)'
                ' VALUES (?, ?, ?, ?)',
                (firstname, lastname, weight, height, age)
            )
            """
            engine = get_db()
            con = engine.connect()
            con.execute(g.db.table.insert(), firstname=firstname, lastname=lastname, weight=weight, height=height,
                        age=age)
            return redirect(url_for("forms.success"))
    return render_template('forms/index.html')


@bp.route("/success", methods=('GET', 'POST'))
def success():
    if request.method == 'POST':
        error= None
    return render_template('forms/success.html')

