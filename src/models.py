import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50),nullable=False) 
    last_name = Column(String(50),nullable=False)
    nickname = Column(String(20),unique=True) 
    email = Column(String(120), nullable=False, unique= True)
    password = Column(String(20), nullable=False)



class Post(Base):
    __tablename__ = 'post'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comments = Column(String(1000), nullable=False)
    #publisher_ID = Column(Integer, ForeignKey('user.id')) REVISAR PORQUE NO FUNCIONA
    image = Column(String(400), nullable=False)
    user = relationship(User)
    

class Comments(Base):
    __tablename__ = 'comments'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    text = Column(String(4000), nullable=False)
    user = relationship(User)
    post = relationship(Post)


class Followers(Base):
    __tablename__ = 'followers'
   
    id = Column(Integer, primary_key=True)
    user_from = Column(Integer, ForeignKey('user.id'))
    user_to = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Likes(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)
    

    def to_dict(self):
        return {}


render_er(Base, 'diagram3.png')