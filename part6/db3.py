from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Corrected the space in the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///stu1.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Capitalized the class name
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    div = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Student('{self.name}','{self.div}')"

if __name__ == "__main__":
    app.run(debug=True)
