from flask import Flask, render_template, request, redirect, session, flash     
app = Flask(__name__)
app.secret_key= "secretkey"

@app.route('/')     
def index():
    return render_template('/index.html')

@app.route('/form', methods=['post'])
def form():
    if len(request.form['first_name']) < 1:
        flash("First Name Required")
    if len(request.form['last_name']) < 1:
        flash("Last Name Required")
    if len(request.form['email']) < 1:
        flash("Email Required")
    if len(request.form['password']) < 1:
        flash("Password Required")
    if len(request.form['confirm_pw']) < 1:
        flash("Password Confirm Required") 
    elif request.form['password'] != request.form['confirm_pw']:
		flash('Passwords do not match, please enter again!')
    else:
        flash('thanks!')
    return redirect('/')


app.run(debug=True)