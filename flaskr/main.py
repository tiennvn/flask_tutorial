from flask import Flask, request

app = Flask(__name__)
# test

@app.route('/')
def hello():
    return 'Hello, World'