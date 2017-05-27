from flask import Flask, render_template, request, redirect, session
import re
app = Flask(__name__)
app.secret_key = 'WhatWhat'
@app.route('/')
def index():
    session.clear()
    if 'display_form' not in session:
        session['display_form'] = 'display: block'
        session['display_image'] = 'display: none'
    return render_template("index.html")

def email_validation(email):
    if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
        return False
    return True


@app.route('/register', methods=['POST'])
def submit_survey():
    if str.isalpha(str(request.form['first_name'])):
        session['first_name'] = request.form['first_name'].strip()
    else:
        session['first_name'] = 'THAT IS NOT YO NAME SUCKA'
        session['display_form'] = 'display: none'
        session['display_image'] = 'display: block'
    if str.isalpha(str(request.form['last_name'])):
        session['last_name'] = request.form['last_name'].strip()
    else:
        session['last_name'] = 'THAT IS NOT YO NAME SUCKA'
        session['display_form'] = 'display: none'
        session['display_image'] = 'display: block'
    if email_validation(request.form['email']):
        session['email'] = request.form['email']
    else:
        session['email'] = 'INVALID EMAIL ADDRESS'
        session['display_form'] = 'display: none'
        session['display_image'] = 'display: block'
    if request.form['password'] == request.form['pass_conf']:
        session['password'] = request.form['password']
        session['pass_conf'] = request.form['pass_conf']
    else:
        session['password'] = 'MAKE DAT SHIT MATCH FOOL'
        session['pass_conf'] = 'MAKE DAT SHIT MATCH FOOL'
        session['display_form'] = 'display: none'
        session['display_image'] = 'display: block'
    print session['first_name']
    print session['last_name']
    print session['email']
    print session['password']
    print session['pass_conf']

    return redirect('/')

app.run(debug=True)
