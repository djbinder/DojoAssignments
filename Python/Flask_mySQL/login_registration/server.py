from flask import Flask, request, redirect, render_template, session, flash
import md5
import re
import os, binascii
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "KeepItSecret"
mysql = MySQLConnector(app,'login_registration')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login_submit.html')

@app.route('/login_submit', methods=['POST'])
def login_submit():
    error = None
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user_b = mysql.query_db(user_query, query_data)
    if len(user_b) != 0:
        encrypted_password = md5.new(password + user_b[0]['salt']).hexdigest()
    if user_b[0]['password'] == encrypted_password:
        flash("correct password")
    if len(email) < 1:
        flash('Email Address Requred to Log In')
    else:
        flash('Incorrect password. Please try again')
    return render_template('login_submit.html')

@app.route('/create', methods=['POST'])
def create():
    error = None
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    salt =  binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()
    if len(request.form['first_name']) < 3:
            flash("First name must be at least 3 characters long")
    if len(request.form['last_name']) < 3:
            flash("Last name must be at least 3 character long")
    if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
    if len(request.form['password']) < 8:
            flash("Password must be greater than 8 characters")
    if (request.form['password']) != (request.form['password_confirm']):
            flash("Passwords do not match")
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW(), NOW())"
        data = {
                        'first_name': first_name,
                        'last_name': last_name, 
                        'email': email,
                        'hashed_pw': hashed_pw,
                        'salt': salt
                    }
        mysql.query_db(query,data)
        flash("Your profile has been created successfully")
    return redirect('/')
app.run(debug=True)