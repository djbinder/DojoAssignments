from flask import Flask, render_template, request, redirect
app = Flask(__name__)                  


@app.route('/')                           
def index_page():
  return render_template("index_whats_my_name.html")


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    return name
    return render_template("process.html", name='name')
    return redirect('/')


app.run(debug=True)