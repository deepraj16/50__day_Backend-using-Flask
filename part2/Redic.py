from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return f'<h1>Wellcome to home page hellow!!</h1>'

@app.route('/failed')
def failed():
    return "<h1>---sorrry you are failed--</h1>"

@app.route('/passed')
def passed():
    return "<h1>---you are passed--</h1>"

@app.route('/score/<int:mark>')
def score(mark):
    if (mark <30):
        return redirect(url_for('failed'))
    else:
        return redirect(url_for('passed'))
    

if __name__ == '__main__':
    app.run(debug=True)