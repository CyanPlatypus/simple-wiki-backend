from flask import Flask

from flaskr import create_app

# app = Flask(__name__)
app = create_app()

@app.route('/')
def hello_test():
    a = 'hi'
    return a