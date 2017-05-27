from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'WhatWhat'
@app.route('/')
def index():
    session['counter']
    session['counter'] += 1
    return render_template("index.html")

@app.route('/refresh', methods=['POST'])
def add_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = -1
    return redirect('/')
app.run(debug=True)
