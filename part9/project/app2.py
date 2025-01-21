from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
import pandas as pd
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load the CSV file
FILE_PATH = "vnn.csv"  # Replace with your actual file path
df = pd.read_csv(FILE_PATH)

# SQLite database configuration
DATABASE = 'database.db'

def init_db():
    """Initialize the database."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Vulnerabilities TEXT,
                links TEXT
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index3.html')

@app.route('/upload_to_db', methods=['POST'])
def upload_to_db():
    """Read CSV data and store it in the SQLite database."""
    if not os.path.exists(FILE_PATH):
        flash(f"File {FILE_PATH} not found.")
        return redirect(url_for('index'))
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Insert CSV data into the database
        for _, row in df.iterrows():
            cursor.execute('''
                INSERT INTO records (Vulnerabilities, links)
                VALUES (?, ?)
            ''', (row['Vulnerabilities'], row['links']))

    flash("Data successfully uploaded to the database!")
    return redirect(url_for('index'))

@app.route('/get_info', methods=['POST'])
def get_info(): 
    """Handle queries for getting information."""
    r = request.form.get('query', '').strip()
    return render_template("index.html", query=r)

@app.route('/search', methods=['POST'])
def search():
    """Perform a search across all columns in the CSV data."""
    query = request.form.get('query', '').strip()
    if query:
        results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
        return render_template('index.html', results=results.to_dict(orient='records'), query=query)
    else:
        return render_template('index3.html', results=[], query=query, message="Please enter a search term.")

@app.route('/suggest', methods=['GET'])
def suggest():
    """Provide suggestions based on the query."""
    query = request.args.get('query', '').strip()
    if query:
        suggestions = df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)
        suggestion_list = df.loc[suggestions, 'Vulnerabilities'].drop_duplicates().tolist()
        return jsonify(suggestions=suggestion_list[:5])
    return jsonify(suggestions=[])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
