from flask import Flask , request , jsonify , json , Response ,make_response
from flask_cors import cross_origin,CORS
import logging
from models import Books , app ,db
from books.views import *
@app.route('/')
def main():
    return "hello asdworld"
@app.route('/addbook',methods=['POST'])
def addbookroute():
    return addbook()
@app.route('/getbooks',methods=['GET'])
def getbookroute():
    return getbooks()

@app.route('/deletebook/<int:book_id>',methods=['DELETE'])
def deletebookroute(book_id):
    return deletebook(book_id)

