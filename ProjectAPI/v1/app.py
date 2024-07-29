from flask import Flask,request,jsonify

app=Flask(__name__)

# DATA
products={}
# routes
@app.route('/product',method=['GET'])
def product():
    if request.method=='GET':
        if len(products)>0:
            return jsonify(products)
        else:
            'Nothing Fount',404

if __name__=='__main__':
    app.run()



