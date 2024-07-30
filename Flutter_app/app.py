from flask import Flask, render_template, abort, url_for, jsonify
import json

app = Flask(__name__, template_folder='.')

# Load JSON data
with open('file.json', 'r') as f:
    data = json.load(f)

# Routes
@app.route('/')
def index():
    return render_template('index.html', title='page', jsonfile=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

