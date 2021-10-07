from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)           
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)