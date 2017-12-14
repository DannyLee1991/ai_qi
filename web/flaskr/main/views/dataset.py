from flask import render_template, make_response
from .. import main


@main.route('/dataset')
def dataset():
    resp = make_response(render_template('dataset.html'))
    return resp
