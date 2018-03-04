from flask import Flask, render_template, request, redirect
from flask_wtf import Form
app = Flask(__name__)                  


@app.route('/')                           
def index_page():
  return render_template("index_dojo_survey.html")


@app.route('/result', methods=['POST'])
def result():
    full_name = request.form['full_name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template("result.html", name=full_name, location=location, language=language, comments=comments)
    return redirect('/')


app.run(debug=True)


# , location='location', language='language', comments = 'comments')
    
    # language = request.form['language']
    # comments = request.form['comments']




    # return name
    # return location
    # return language
    # return comments