import requests
import datetime
from flask import Flask,render_template


app = Flask(__name__)


@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    date = datetime.datetime.now().year
    return render_template(
        "index.html",
        user=name, age=age_response.json()["age"],
        gender=gender_response.json()["gender"],
        year=date
    )


if __name__ == "__main__":
    app.run(debug=True)
