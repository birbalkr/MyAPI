from flask import(Flask, render_template, abort, url_for, json, jsonify)
 

app=Flask(__name__, template_folder='.')
with open('file.json','r') as f:
    data=f.read()


# routes
@app.route('/')
def index():
    return render_template('index.html',title='page',jsonfile=json.dump(data))

if __name__=='__main__':
    app.run()



