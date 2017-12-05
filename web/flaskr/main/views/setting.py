from flask import render_template, make_response
from .. import main


@main.route('/setting')
def setting():
    resp = make_response(render_template('setting.html'))
    return resp
