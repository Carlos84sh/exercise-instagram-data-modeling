import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(100), nullable=False)
    user_name = Column(String(20),unique=True)
    dob = Column(db.DateTime)
    telephone = Column(Integer)
    gender = Column(String(10),nullable=False)


class Post(Base):
    __tablename__ = 'address'
   
    id = Column(Integer, primary_key=True)
    user_name = db.Column(db.Integer, db.ForeignKey('User.user_name'))
    comments = Column(String(250))
    mp4 = Column(String(250))
    post_date = Column(db.DateTime)
    publisher_ID = db.Column(db.Integer, db.ForeignKey('User.id'))
    

class Comments(Base):
    __tablename__ = 'address'
   
    id = Column(Integer, primary_key=True)
    user_name = db.Column(db.Integer, db.ForeignKey('Post.user_name'))
    comments = db.Column(db.Integer, db.ForeignKey('Post.comments'))
    comment_date = Column(db.DateTime)


class Followe(Base):
    __tablename__ = 'address'
   
    id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user_name = Column(String(20))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')