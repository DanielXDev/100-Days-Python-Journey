# save this as app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"

#routing using app.route decorator
@app.route("/login")
def login():
    return "Login to your account"

#creating variable path and converting path to a specific data type
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are No {number}"


if __name__ == '__main__':
    app.run(debug=True)