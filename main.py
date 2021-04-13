from flask import Flask , request , jsonify , json , Response 
from flask_cors import cross_origin,CORS
from models import Books ,app , db
import logging
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def main():
    return "hello asdworld"
@app.route('/addbook',methods=['POST'])
def addbook():
    #print(request.json,type(request.form))
    book = Books(authors=request.json["authors"],isbn=request.json["isbn"],stock=request.json["stock"],title=request.json["title"])
    db.session.add(book)
    db.session.commit()
    logging.basicConfig(level=logging.DEBUG)
    print(request.host,"request")
    return "Response.status"
@app.route('/getbooks',methods=['GET'])
def getbooks():
    data = Books.query.all()
    data2 = []
    for element in data:
        elm = {
            'id':element.id,
            'title':element.title,
            'authors' : element.authors,
            'isbn': element.isbn , 
            'stock' : element.stock
        }
        data2.append(elm)
    return jsonify(thelist = data2)
