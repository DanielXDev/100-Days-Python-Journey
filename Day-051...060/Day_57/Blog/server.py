import smtplib
import requests
import datetime
import json
import os
import urllib.parse
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

@app.route("/")
def homepage():
    response = requests.get("https://api.npoint.io/13d8592e07bc65702c4a")
    all_blogs = response.json()
    year = datetime.datetime.now().year
    return render_template("index.html", blogs=all_blogs, year=year)

@app.route("/blog/<num>")
def get_blog(num):
    content = request.args.get('content')
    
    # Check if the 'content' parameter is missing
    if not content:
        return "Error: Missing 'content' query parameter.", 400  # HTTP 400 Bad Request

    try:
        # Attempt to decode and parse the JSON content
        content_dict = json.loads(urllib.parse.unquote(content))
    except (json.JSONDecodeError, TypeError) as e:
        return f"Error: Invalid 'content' parameter. {str(e)}", 400  # HTTP 400 Bad Request

    # Safely access the title and render the template
    print(content_dict.get("title", "No title provided"))
    year = datetime.datetime.now().year
    return render_template("blog.html", blog=content_dict, year=year)

@app.route("/about")
def about():
    year = datetime.datetime.now().year
    return render_template("about.html", year=year)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    year = datetime.datetime.now().year

    #Check if user is sending a message
    if "message" in request.form:
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        my_email = os.getenv("MY_EMAIL")
        password = os.getenv("PASSWORD")

        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=my_email,
                msg=f"Subject: Message!!!\n\n Name:{name} \n Email:{email} \n Message:{message}"
            )
    return render_template("contact.html", year=year)


if __name__ == "__main__":
    app.run(debug=True)
