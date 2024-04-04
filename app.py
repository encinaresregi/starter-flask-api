from flask import Flask, make_response
import os

app = Flask(__name__)

@app.route('/')
def home():
    resp = make_response("hello") #here you could use make_response(render_template(...)) too
    resp.headers['Sample-header'] = '1103'
    return resp
