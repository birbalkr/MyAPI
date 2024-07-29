from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'hello' 

# progammatically
if __name__=='__main__':
    app.run()
# run 
# python app.py

# Dynamic Routing
@app.route('/<name>')
def print_name(name):
    return 'Hii, {}'.format(name)