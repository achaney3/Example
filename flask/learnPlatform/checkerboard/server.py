from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')          
def checkereight():
    return render_template("index.html",row=8, col=8)

@app.route('/<row>')          
def checkerrow(row):
    return render_template("index.html",row=int(row), col=8)

@app.route('/<row>/<col>')          
def checkerdynqamic(row, col):
    return render_template("index.html",row=int(row), col=int(col))

if __name__=="__main__":   
    app.run(debug=True)   