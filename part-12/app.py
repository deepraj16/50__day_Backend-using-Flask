from flask import Flask, render_template, request, redirect, url_for
from models import db, Book
from config import DATABASE_URL

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_book.html")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_book(id):
    book = Book.query.get(id)
    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("update_book.html", book=book)

@app.route("/delete/<int:id>")
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
