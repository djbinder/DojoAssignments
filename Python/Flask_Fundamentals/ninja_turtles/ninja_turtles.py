from flask import Flask, render_template, request, redirect
app = Flask(__name__)                  


@app.route('/')                           
def index_page():
  return 'No Ninjas Here'


@app.route('/ninjas')
def ninjas_pictures():
    return render_template('ninjas.html')

@app.route('/ninjas/blue')
def ninjas_blue():
    return render_template('leonardo.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('april.html'), 404



app.run(debug=True)