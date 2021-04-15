from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.schema import Table , Column
from flask_cors import CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True ,nullable=False)
    title = db.Column(db.String ,nullable=False)
    authors = db.Column(db.String , nullable=False)
    isbn = db.Column(db.String )
    stock = db.Column(db.Integer,nullable=False)
    def __str__(self):
        return '<Book %r>' % self.id
class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True ,nullable=False)
    first_name = db.Column(db.String ,nullable=False)
    last_name = db.Column(db.String ,nullable=False)
    debt = db.Column(db.Integer, primary_key=True ,nullable=False )
transactions = db.Table('transactions',db.Column('members_id', db.Integer, db.ForeignKey('members.id'), primary_key=True ,nullable=False),db.Column('books_id', db.Integer, db.ForeignKey('books.id'), primary_key=True ,nullable=False),db.Column('id', db.Integer, primary_key=True ,nullable=False))

