# -*- coding: utf-8 -*-
from ../app import app
from flask import render_template, flash, request, redirect, url_for
from flaskext.couchdb import paginate
from ../models.Signature() import Signature


@app.route('/')
def display():
    page = paginate(Signature.all(), 5, request.args.get('start'))
    return render_template('display.html', page=page)


@app.route('/', methods=['POST'])
def post():
    message = request.form.get('message')
    author = request.form.get('author')
    if not message or not author:
        flash("You must fill in both a message and an author")
    else:
        signature = Signature(message=message, author=author)
        signature.store()
        flash("Signature stored")
    return redirect(url_for('display'))