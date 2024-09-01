from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return f'<h1>Wellcome to home page hellow!!</h1>'

@app.route('/failed/<sname>/<int:marks>')
def failed(sname,marks):
    return f"<h1>---sorrry {sname} you are failed--</h1>"

@app.route('/passed/<sname>/<int:marks>')
def passed(sname , marks):
    return f"<h1>---you are passed {sname}--</h1>"

@app.route('/score/<name>/<int:mark>')
def score(name,mark):
    if (mark <30):
        return redirect(url_for('failed',sname=name,marks=mark))
    else:
        return redirect(url_for('passed',sname=name,marks=mark))
    

if __name__ == '__main__':
    app.run(debug=True)