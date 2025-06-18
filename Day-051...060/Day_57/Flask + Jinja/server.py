import random
import datetime
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def homepage():
    random_num = random.randint(0, 10)
    date = datetime.datetime.now()
    current_year = date.year
    return render_template("index.html", num= random_num, year=current_year)



if __name__ == "__main__":
    app.run(debug=True)