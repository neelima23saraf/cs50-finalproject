
#for sending the mail start
import os
import re
from flask_mail import Mail, Message
#for sending the mail ends

from flask import Flask, render_template, redirect, request
app = Flask(__name__)

#for sending the mail start
app.config["MAIL_DEFAULT_SENDER"] = "parallellinesnmadhubani@gmail.com"
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_USERNAME"] = "parallellinesnmadhubani@gmail.com"

mail = Mail(app)

#for sending the mail ends


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/fish")
def fish():
    return render_template("fish.html")

@app.route("/birds")
def birds():
    return render_template("birds.html")

@app.route("/animals")
def animals():
    return render_template("animals.html")

@app.route("/god")
def god():
    return render_template("god.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
         # Validate submission
        name = request.form.get("name")
        email = request.form.get("email")
        description = request.form.get("message")
        # if not email or message:
        #     return render_template("failure.html")
        # else:
            # Send email

        message = Message(subject=name, body=description, recipients=[email])
        
        mail.send(message)
        return render_template("success.html")
    else:
        return render_template("contact.html")
