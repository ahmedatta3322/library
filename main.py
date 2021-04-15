from flask import Flask , request , jsonify , json , Response ,make_response
from flask_cors import cross_origin,CORS
import logging
from models import Books , app ,db
@app.route('/')
def main():
    return "hello asdworld"
@app.route('/addbook',methods=['POST'])
def addbook():
    response = make_response()
    try:  
        book = Books(authors=request.json["authors"],isbn=request.json["isbn"],stock=request.json["stock"],title=request.json["title"])
        try:
            db.session.add(book)
            db.session.commit()
            response.data = "Request succeed and saved to the database"
            response.status = "200"
        except:
            response.data = "Request failed" 
            response.status = "401"
        return response 
    except Exception as e:
        response.data = "Please provide valid" + str(e) 
        response.status = "500"
        return response
@app.route('/getbooks',methods=['GET'])
def getbooks():
    books = Books.query.all()
    bookslist = []
    for element in books:
        elm = {
            'id':element.id,
            'title':element.title,
            'authors' : element.authors,
            'isbn': element.isbn , 
            'stock' : element.stock
        }
        bookslist.append(elm)
    return jsonify(thelist = bookslist)
