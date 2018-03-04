from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


counter = 1
 
@app.route("/")
def index():
    global counter
    counter = counter + 1
    return str(counter)


app.run(debug=True)