from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>welcome to my home page </h1>"

@app.route('/about/deepraj')
def string():
    return "<h1>welcome deepraj</h1>"
#it is very defficl to get for avery time from avery user so we have to work on the 
#dynamic page work

@app.route('/about/ram')
def string1():
    return "<h1>welcome ram</h1>"

@app.route('/about/omkar')
def string2():
    return "<h1>welcome omkar</h1>"


if __name__=='__main__':
    app.run(debug=True)