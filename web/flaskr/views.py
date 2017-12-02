from flask import Flask, render_template, make_response

from . import manager

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    manager.fs_stock()
    return resp