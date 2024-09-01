from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file(r'C:\Users\raj\Flask-Course\part1\prac2.html')

@app.route('/about')
def about():
    return "<p>This is about page</p>"

@app.route('/contact')
def contact():
    return "my name is deepraj"

@app.route("/string/<str1>")
def string(str1):
    return f"<h1>hi {str1} is given</h1>"

@app.route("/addation/<int:num1>")
def addation(num1):
    return f"<h1>input {num1} output is {num1 + 1}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
