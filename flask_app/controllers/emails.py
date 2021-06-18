from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route("/")
def input_email():
    return render_template("email.html")

@app.route("/validate_email", methods=["POST"])
def validate():
    if not Email.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/create')

@app.route("/create")
def create_email():
    Email.create(request.form)
    return redirect("/show/emails")