from flask import Flask, render_template
app = Flask(__name__)                     


@app.route('/')                           
def index_page():
  return render_template("landing_page_index.html")


@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojos/')
def dojos():
    return render_template("dojos.html")


app.run(debug=True)