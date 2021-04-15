from models import Books , app ,db
from flask import Flask , request , jsonify , json , Response ,make_response
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
def deletebook(book_id):
    response = make_response()
    try:
        book = Books.query.get(book_id)
        if(book != None):
            try:
                db.session.delete(book)
                db.session.commit()
                response.data = "Success deleting" + "  " +book.title
            except:
                response.data = "can't delete the book"
        else :
            response.data = "can't find a book"
    except:
        response.data = "unkown error"
    return response
    