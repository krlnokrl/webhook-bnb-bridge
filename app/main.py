from flask import Flask, json


app = Flask(__name__)


@app.route('/')
def index():
  return 'Testing...'
