import os, sys
from flask import Flask

sys.path.append('libs')
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from arvind!'
