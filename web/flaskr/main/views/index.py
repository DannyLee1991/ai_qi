from flask import render_template, make_response
from .. import main


@main.route('/', methods=['GET', 'POST'])
def index():
    resp = make_response(render_template('index.html'))
    return resp
