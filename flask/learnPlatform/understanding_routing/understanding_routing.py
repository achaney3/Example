from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    print(name)
    return "Hello, " + name + "!"


@app.route('/repeat/<int:number>/<string:name>')
def repeat(number, name):
    return number*name

if __name__=="__main__":  
    app.run(debug=True)    # Run the app in debug mode.
  