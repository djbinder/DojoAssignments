from flask import Flask, render_template
app = Flask(__name__)                     


@app.route('/')                           
def portfolio():
  return """
    <!DOCTYPE HTML>
<html>
    <head>
    </head>
    <body>
        <p>Welcome to my portfolio. My name is Dan BInder.</p>
    </body>
</html>
"""
                     
@app.route('/stanford')
def stanford_page():
    return """
      <h1>Hello stanford! stanford</h1>
    """    


@app.route('/project')
def project():
  return render_template('project.html')
  return """<h1>Hello stanford! project</h1>"""


@app.route('/about')
def about():
  return render_template('about.html')





app.run(debug=True)  


