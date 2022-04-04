# Import what we need from flask
from flask import Flask

app = Flask("__name__")

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/cow')
def cow():
    return 'MOoooOo!'
    
