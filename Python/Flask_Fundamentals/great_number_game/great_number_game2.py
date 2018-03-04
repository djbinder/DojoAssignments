from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def secretnumber():
    global secretnumber
    secretnumber = random.randrange(0,100)
    print secretnumber

@app.route("/")
def index():
    secretnumber()
    print secretnumber
    return render_template("great_num_game_index.html", secretnumber=secretnumber)

@app.route("/guess", methods=['POST'])
def result ():
    if int(request.form['guess']) == secretnumber:
        answer = "YOU GOT IT!"
        return render_template("great_num_game_index.html", answer=answer, secretnumber=secretnumber)
    elif int(request.form['guess']) < secretnumber: 
        answer = "Too Low. Guess Again."
        return render_template("great_num_game_index.html", answer=answer, secretnumber=secretnumber)
    else:
        answer = "Too High. Guess Again"
        return redirect("/")


app.run(debug=True)