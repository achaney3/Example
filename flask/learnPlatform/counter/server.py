from flask import Flask, render_template, request,session, redirect 
app = Flask(__name__)  
app.secret_key = 'learningsession!'

@app.route('/')
def index ():
    if "views" in session:
        session["views"] += 1
    else: 
        session['views'] = 0
    return render_template('index.html')

@app.route('/count')
def count():
    if 'views' in session:
        session['views'] = session.get('views') + 1
    return redirect ('/')

@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")


if __name__=="__main__":   
    app.run(debug=True)   
