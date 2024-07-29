from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'hello API' 
# Linux
# export FLASK_APP=app.py
# Window
# set FLASK_APP=app.py
# flask run