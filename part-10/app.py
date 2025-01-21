from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "1234"
DB_NAME = "crud_db"

# Database connection function
def get_db_connection():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Home route - Display all records
@app.route('/')
def index():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    connection.close()
    return render_template('index.html', users=users)

# Route for adding a new user
@app.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            connection.commit()
        connection.close()

        flash("User added successfully!")
        return redirect(url_for('index'))

# Route for editing a user
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    connection = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        with connection.cursor() as cursor:
            cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, id))
            connection.commit()
        connection.close()

        flash("User updated successfully!")
        return redirect(url_for('index'))
    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
            user = cursor.fetchone()
        connection.close()
        return render_template('edit.html', user=user)

# Route for deleting a user
@app.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id=%s", (id,))
        connection.commit()
    connection.close()

    flash("User deleted successfully!")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
