from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:/// IPL.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =SQLAlchemy(app)

#create to tables 1)ipl 2)ipl player tables
class Team(db.Model):
    __tablename__ ='teams'
    id = db.Column(db.Integer,primary_key=True)
    team =db.Column(db.String(50),nullable=False,unique=True)
    state=db.Column(db.String(50),nullable=False)

    members =db.relationship('Player',backref='team') ## backref create an imager instant in
    ##in Player colums
    


    def __repr__(self):
        return f"Team('{self.team}','{self.state}')"



class Player(db.Model):
    __tablename__ ='player'
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(50),nullable=False,unique=True)
    nation=db.Column(db.String(50),nullable=False)
    team_id =db.Column(db.Integer,db.ForeignKey('teams.id'))
    ## to sql alcamy
  

    def __repr__(self):
        return f"Player('{self.name}','{self.nation}')"
    




if __name__ =='__main__':
    app.run(debug=True)