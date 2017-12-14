from flask import render_template, make_response
from .. import main


@main.route('/models', methods=['GET'])
def models():
    resp = make_response(render_template('models.html'))
    return resp
