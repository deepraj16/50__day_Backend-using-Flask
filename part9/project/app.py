from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load the Excel file
FILE_PATH = "vnn.csv"  # Replace with your file path
df = pd.read_csv(FILE_PATH)

@app.route('/')
def index():
    return render_template('index.html','GET')

@app.route('/get_info',methods=['POST',])
def get_info(): 
    r=request.form.get('query', '').strip()
    return render_template("index.html",r)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').strip()
    if query:
        # Case-insensitive search across all columns
        results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
        return render_template('index.html', results=results.to_dict(orient='records'), query=query)
    else:
        return render_template('index.html', results=[], query=query, message="Please enter a search term.")

@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('query', '').strip()
    if query:
        suggestions = df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)
        suggestion_list = df.loc[suggestions].iloc[:, 0].drop_duplicates().tolist()  # Suggest from the first column
        return jsonify(suggestions=suggestion_list[:5])
    return jsonify(suggestions=[])

if __name__ == '__main__':
    app.run(debug=True)
