from flask import Flask,render_template,url_for
import employ as em

app=Flask(__name__,template_folder='templates',)
# today topic
# 1)paramerter and placeholder
# 2)if condition
# 3)for loop 
# 4)Blocks

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="home")

@app.route('/about')
def about():
    return render_template('about.html',title="aboutraj")

@app.route('/contact')
def contact1():
    return render_template('contact.html',title='contact')

@app.route('/contain')
def contain1():
    return render_template('con1.html',title='con1')
# how to use jnja for if,and looping condition
@app.route('/evaluate/<int:num>')
def check(num):
    #parthparameter
    return render_template('evaluate.html',title="Evaluate",number=num )


@app.route('/employees')
def employees():
    return render_template('employee.html',title="data",employee= em.employees_data )

#information in for of table form so that we can use it again
@app.route('/tableinfo')
def info():
    return render_template('table.html',title="data",employee= em.employees_data)

# information of only manger in given form
@app.route('/employees/manger')
def manger():
    return render_template('manger.html',title='manger',employee= em.employees_data)
if __name__ == '__main__':
    app.run(debug=True)