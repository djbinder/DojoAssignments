from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)                  
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')                           
def index():
  return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    full_name = request.form['full_name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    if len (request.form['full_name']) < 1: 
        flash("Name Cannot be Empty!")
    if len (request.form['comments']) > 120:
        flash("Comments must be less than 120 characters")
    else:    
        return render_template("result.html", name=full_name, location=location, language=language, comments=comments)
    return redirect('/')


app.run(debug=True)