from flask import Flask,render_template,url_for,redirect,flash

app = Flask(__name__)

from forms import SignupFrom,LoginFrom

app.config['SECRET_KEY'] = 'this_is_key'
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/signup',methods=["GET","POST"]) #get methods is import for geting data from users
#the for will submit
def signup():
    forms =SignupFrom()
    if forms.validate_on_submit():
        flash(f"Successfully Registered { forms.username.data }")
        return redirect(url_for('home'))
    return render_template('signup.html',title ='Signup',form=forms)

# @app.route('/Login')
# def login():
#     forms =LoginFrom()
#     return render_template('login.html',title='Login',form=forms)

@app.route("/Login", methods=["GET", "POST"])
def login():
    form = LoginFrom()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        if email == "a@b.com" and pw == "12345":
            flash("Logged in Successfully!")
            return redirect(url_for("home"))
        else:
            flash("Incorrect email or password")
    return  render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)