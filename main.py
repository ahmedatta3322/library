from flask import Flask , request , jsonify , json
from models import Books ,app
@app.route('/')
def main():
    return "hello asdworld"
@app.route('/addbook',methods=['POST'])
def addbook():
    print(request.data)
    return "axzcadassd"
@app.route('/getbooks',methods=['POST','GET'])
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
        
    
    #jsonify(json_list = data)
    print(data2)
    return jsonify(thelist = data2)