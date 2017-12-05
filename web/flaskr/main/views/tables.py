from flask import render_template, make_response
from .. import main


@main.route('/tables')
def tables():
    resp = make_response(render_template('tables.html'))
    return resp
