from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def homepage():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
            )

@app.route("/<int:number>")
def user_guess(number):
    answer = random.randint(0, 10)
    if number > answer:
        return ("<h1 style='color: red'>Too high, try again!!</h1>" 
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
                )
    elif number < answer:
        return ("<h1 style='color: black'>Too low, try again!!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
                )
    else:
        return ("<h1 style='color: green'>You found me</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
                )

if __name__ == "__main__":
    app.run(debug=True)