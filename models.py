from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.schema import Table , Column
from flask_cors import CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
CORS(app)
db = SQLAlchemy(app)
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    authors = db.Column(db.String)
    isbn = db.Column(db.String)
    stock = db.Column(db.Integer)
    def __str__(self):
        return '<Book %r>' % self.id
class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    debt = db.Column(db.Integer, primary_key=True)
transactions = db.Table('transactions',db.Column('members_id', db.Integer, db.ForeignKey('members.id'), primary_key=True),db.Column('books_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),db.Column('id', db.Integer, primary_key=True))


#class Transactions(db.Model):
#    id = Column(db.Integer, primary_key=True)
#    data = db.relationship('Members', secondary=books_members, lazy='subquery',backref=db.backref('books', lazy=True))
    
    

