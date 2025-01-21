# app.py
from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Book
from config import Config
from datetime import datetime


# base.html        # Base HTML template
# │   ├── add_book.html    # Form to add a new book
# │   ├── edit_book.html   # Form to edit a book
# │   └── book_list.html

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

app.config['SECRET_KEY'] = 'mysecretkey'
with app.app_context():
    db.create_all()

@app.route('/')
def book_list():
    books = Book.query.all()
    return render_template('book_list.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pub_date = datetime.strptime(request.form['pub_date'], '%Y-%m-%d')
        new_book = Book(title=title, author=author, pub_date=pub_date)
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!')
        return redirect(url_for('book_list'))
    return render_template('add_book.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.pub_date = datetime.strptime(request.form['pub_date'], '%Y-%m-%d')
        db.session.commit()
        flash('Book updated successfully!')
        return redirect(url_for('book_list'))
    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:id>')
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!')
    return redirect(url_for('book_list'))

if __name__ == '__main__':
    app.run(debug=True)
