from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5





app = Flask(__name__)
app.secret_key = 'myfirstwtform'
csrf = CSRFProtect(app)

bootstrap = Bootstrap5(app)




class MyForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
        if email == "admin@gmail.com" and password == "12345678":
            page = 'success.html'
        else:
            page = 'denied.html'
    else:
        page = 'login.html'
    return render_template(page, form=form)


if __name__ == '__main__':
    app.run(debug=True)
