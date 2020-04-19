from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/rafael")
def rafael():
    return "Hello, Rafael!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}</h1?"
