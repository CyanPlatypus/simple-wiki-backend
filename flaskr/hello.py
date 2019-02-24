from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_test():
    a = 'hi'
    return a