from flask import Flask, render_template, make_response

from . import manager

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    # manager.fs_stock()
    return resp

@app.route('/setting')
def setting():
    resp = make_response(render_template('setting.html'))
    return resp

@app.route('/getdata')
def getdata():
    resp = make_response(render_template('getdata.html'))
    return resp