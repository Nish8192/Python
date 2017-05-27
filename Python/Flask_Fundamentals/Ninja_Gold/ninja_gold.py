from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'WhatWhat'
@app.route('/')
def index():
    # session.clear()
    if 'total_gold' not in session:
        session['total_gold'] = 0
        session['MESSAGE'] = ''
        session['boss'] = 'display: none'

    if session['total_gold'] < 0:
        session['MESSAGE'] = 'PIT BOSS ARRIVES AND BREAKS YOUR KNEE CAPS :('
        session['boss'] = 'display: block'
    print session['total_gold']
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def processDaMoney():

    if request.form['action'] == 'farm':
        session['total_gold'] += random.randrange(10,20)
        print session['total_gold']
        return redirect('/')
    elif request.form['action'] == 'cave':
        session['total_gold'] += random.randrange(5,10)
        print session['total_gold']
        return redirect('/')
    elif(request.form['action'] == 'house'):
        session['total_gold'] += random.randrange(2,5)
        print session['total_gold']
        return redirect('/')
    elif(request.form['action'] == 'casino'):
        session['total_gold'] += random.randrange(-50,50)
        print session['total_gold']
        return redirect('/')
    elif(request.form['action'] == 'reset'):
        session.clear()
        return redirect('/')



app.run(debug=True)
