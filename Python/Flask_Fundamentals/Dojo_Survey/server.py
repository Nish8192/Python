from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'WhatWhat'
@app.route('/')
def index():

    return render_template("index.html")


@app.route('/results', methods=['POST'])
def submit_survey():
    session['error'] = True
    name = request.form['name']
    location = request.form['dojo_location']
    favorite_language = request.form['fav_lang']
    session['addtnl_comments'] = request.form['comments']
    if(len(session['addtnl_comments'])>120):
        session['error'] = True
        return redirect('/')
    else:
        session['error'] = False
        return render_template('result.html', n = name, loc = location, fl=favorite_language)
app.run(debug=True)
