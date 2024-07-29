from flask import Flask, request, jsonify

app=Flask(__name__)

book_list=[
    {
        'id':0,
        'title':'MyBook',
        'language':'Python',
    },
    {
        'id':0,
        'title':'MyBook',
        'language':'Python',
    }
]

@app.route('/books',methods=['GET','PUT'])
def books():
    if request.method=='GET':
        if len(book_list)>0:
            return jsonify(book_list)
        else:
            'Nothing Fount',404
    if request.method=='POST':
        new_title=request.form['title']
        new_lang=request.form['language']
        iD=book_list[-1]['id']+1

        new_obj={
            'id':iD,
            'title':new_title,
            'language':new_lang
        }
        book_list.append(new_obj)
        return jsonify(book_list),201
    

@app.route('/')
def index():
    return 'hello'

if __name__=='__main__':
    app.run()