from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route("/")
def index():
    session['number'] = random.randrange(0,100)
    print session['number']
    return render_template("great_num_game_index.html")

@app.route("/guess", methods=['POST'])
def result ():
    if int(request.form['guess']) == session['number']:
        answer = "YOU GOT IT!"
        return render_template("great_num_game_index.html", answer=answer)
    elif int(request.form['guess']) < session['number']: 
        answer = "Too Low. Guess Again."
        return render_template("great_num_game_index.html", answer=answer)
    else:
        answer = "Too High. Guess Again"
        return render_template("great_num_game_index.html", answer=answer)


app.run(debug=True)