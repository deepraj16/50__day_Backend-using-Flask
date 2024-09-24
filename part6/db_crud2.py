from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///deep.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db=SQLAlchemy(app)

class  d(db.Model):
    sr=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String[20],nullable =False)
    roll=db.Column(db.Integer)

    def __repr__(self):
        return f"d( '{self.name}','{self.roll}' )"

if __name__ == '__main__':
    app.run(debug=True)