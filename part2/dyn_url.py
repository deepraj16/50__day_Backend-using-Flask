from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>welcome to my home page </h1>"

@app.route('/about/<str>')
def string(str):
    return f"<h1>welcome ({str})</h1>"


if __name__=='__main__':
    app.run(debug=True)