from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+[a-zA-Z-]*[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/login', methods=['POST'])
def submit():
    isform_valid= TRUE
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        isform_valid= FALSE
    # else if email doesn't match regular expression display an "invalid email address" message
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        isform_valid= FALSE
    elif len(request.form['fname']) < 3:
        flash(" Name should have more than two characters")
        isform_valid= FALSE
    elif not NAME_REGEX.match(request.form['fname']):
        flash("First Name cannot contain numbers!")
        isform_valid= FALSE
    elif len(request.form['lname']) < 3:
        flash(" Name should have more than two characters")
        isform_valid= FALSE
    elif not NAME_REGEX.match(request.form['lname']):
        flash("Last Name cannot contain numbers!")
        isform_valid = FALSE
    elif len (request.form['password']) < 8:
        flash("password should be atleast 8 characters")
        isform_valid = FALSE
    elif not (request.form['password']) == (request.form['password_confirmation']):
        flash("password should match")
        isform_valid= FALSE
    else:
        if form_validisform_valid:
        flash("Thanks for sumitting the correct information user!")
    fullname = request.form['fname'] + request.form['lname']
    # return render_template('success.html', name = fullname) 
    return redirect('/')

app.run(debug=True)

	
