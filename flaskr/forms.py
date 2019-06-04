import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('forms', __name__)

@bp.route('/')
def index():
    if request.method == 'POST':
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        weight = request.form['weight']
        height = request.form['height']
        error = None

        if not firstname:
            error = 'First name is required.'
        if not lastname:
            error = 'Last name is required'
        if error is not None:
            flash(error)
        """
        else:
            db = get_db()
            db.execute(
                'INSERT INTO info (firstname, lastname, weight, height,)'
                ' VALUES (?, ?, ?, ?)',
                (firstname, lastname, weight, height)
            )
            db.commit()
            return redirect(url_for('blog.index'))
        """
    return render_template('forms/index.html')
