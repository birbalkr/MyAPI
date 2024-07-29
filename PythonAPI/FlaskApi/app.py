from flask import Flask, request, jsonify
import json, sqlite3

app=Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/books',methods=['GET','POST'])
def books():
    conn=db_connection()
    cursor = conn.cursor()


    if request.method=='GET':
            cursor=conn.execute('SELECT * FROM book')
            books=[
                 dict(id=row[0],author=row[1],language=row[2],title=row[3])
                 for row in cursor.fetchall()
            ]
            if books is not None:
                 return jsonify(books)
    if request.method=='POST':
        new_author=request.form['author']
        new_title=request.form['title']
        new_lang=request.form['language']
        sql="""INSERT INTO book(author,title,language)
        VALUES(?, ?, ?)"""
        cursor = cur.execute(sql,(new_author,new_lang,new_title))
        conn.commit()
        return f"Book with the id:{cursor.las}"


@app.route('/')
def index():
    return 'hello'

if __name__=='__main__':
    app.run()