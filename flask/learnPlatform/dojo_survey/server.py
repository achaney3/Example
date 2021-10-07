from flask import Flask, render_template, session, redirect, request
from flask.templating import render_template_string
app = Flask(__name__)
app.secret_key = 'hithere'

@app.route('/')
def createuser():
    return render_template ("index.html")

@app.route('/process', methods=['POST', 'GET'])
def process():
    print('processing')
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['timezone'] = request.form['timezone']
        session['favlanguage'] = request.form['favlanguage']
        session['comment'] = request.form['comment']
        return redirect('/results', name=request.form['name'])
    else:
        return render_template ("index.html")

@app.route('/results')
def results():
    print('results')
    return render_template("results.html")





if __name__=="__main__":
    app.run(debug=True)