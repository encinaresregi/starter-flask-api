from flask import Flask, make_response
import os

app = Flask(__name__)

@app.route('/')
def home():
    data = ""
    resp = make_response("hello") #here you could use make_response(render_template(...)) too
    resp.headers['Sample-header'] = '1103'
    resp.headers['Content-Type'] = 'application/x-x509-ca-cert'
    resp.headers['Content-Length'] = len(data)
    resp.headers['Connection'] = "close"
    return resp
