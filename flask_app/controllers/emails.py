from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route("/")
def input_email():
    return render_template("email.html")

@app.route("/validate_email", methods=["POST"])
def validate():
    if not Email.validate_email(request.form):
        print("validation failed")
        return redirect('/')
    print("validation success!")
    Email.create(request.form)
    return redirect("/show")

@app.route("/show/")
def show():
    emails = Email.get_all()
    return render_template("show_emails.html", emails = emails)