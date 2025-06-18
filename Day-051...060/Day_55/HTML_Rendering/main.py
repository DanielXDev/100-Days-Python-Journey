from flask import Flask

app = Flask(__name__)



@app.route("/")
def homepage():
    return ("<h1 style='text-align: center'> Hello World </h1>"
            "<p> This is a fucking paragraph </p>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW03Zm1jZHhvOXhuMXRwazVzc2EzbGI5OHpjYW83NmZrZGIwYmQ2OCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/CjmvTCZf2U3p09Cn0h/giphy.gif' width= 200>")
def make_bold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function()}</b>"
    return wrapper

def emphasis(function):
    def wrapper(*args, **kwargs):
        return f"<em>{function()}</em>"
    return wrapper

def underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/bye")
@make_bold
@emphasis
@underline
def bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True)