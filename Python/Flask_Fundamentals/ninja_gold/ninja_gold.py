from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 's3cr3tk3y'


@app.route('/')
def index():
	if not 'gold_count' in session:
		session['gold_count'] = 0
	if not 'log' in session:
		session['log'] = ''
	data = {}
	data['gold_count'] = session['gold_count']
	data['log'] = session['log']
	return render_template('index.html', data=data)

@app.route('/process_money', methods=['POST'])
def process():
    location=request.form['location']
    if location == "farm":
        added_gold = random.randrange(10,21)
        message = "<div class='won'>you win money from the farm" + str(added_gold) + "gold</div>"
    if location == "cave":
        added_gold = random.randrange(5,11)
        message = "<div class='won'>you win money from the cave</div>"
    if location == "house":
        added_gold = random.randrange(2,6)
        message = "<div class='won'>you win money from the house</div>"

	log = session['log']
	session['log'] = message + log
	session['gold_count'] += added_gold
	print session['log']
	return redirect('/')

@app.route('/reset')
def reset():
	session['gold_count'] = 0
	session['log'] = ''
	return redirect('/')

app.run(debug=True)