from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')

app.secret_key = 'WhatWhat'
def email_validation(email):
    if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
        return False
    return True
@app.route('/')
def index():
    query = "SELECT * FROM users"
    session['result'] = mysql.query_db(query)
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def user_login():
    email = request.form['user_name']
    password = request.form['pass']

    user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
    query_data = {'email': email, 'password': password}
    user = mysql.query_db(user_query, query_data)
    print query_data
    return redirect('/')
    # if user:
    #     return render_template('wall.html')
    # else:
    #     return redirect('/register')





@app.route('/register', methods=['GET'])
def registerNewUser():

    return render_template('new_user_registration.html')

@app.route('/add_user', methods=['POST'])
def addNewUser():
    flag = False
    if not str.isalpha(str(request.form['first_name'])):
        flag = True
        flash('Sorry, the first name is not valid, please try again')
    if not str.isalpha(str(request.form['last_name'])):
        flag = True
        flash('Sorry, the last name is not valid, please try again')
    if request.form['password'] != request.form['pass_con']:
        flag = True
        flash('Sorry, the passwords do not match, please try again')

    if not email_validation(request.form['user_email']):
        flag = True
        flash('Sorry, email is not valid, please try again')
    if not flag:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['user_email'],
            'password': request.form['password']
        }
        print data
        mysql.query_db(query, data)

        return redirect('/')
    else:
        return redirect('/register')


app.run(debug=True)
