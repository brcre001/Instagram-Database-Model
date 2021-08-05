import os, datetime
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
# db.Column(Integer, primary_key=True)
# db.Model as the argument for the classes

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(50), nullable=False)
    join_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.first_name

    def serialize(self):
        return {
            "user id": self.user_id,
            "first name": self.first_name,
            "last name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
            "join date": self.join_date
        }

class Posts(Base):
    __tablename__ = 'Posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(250), nullable=True)
    media_source = Column(String(100), nullable=False)
    post_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title

    def serialize(self):
        return {
            "post id": self.post_id,
            "user id": self.user_id,
            "title": self.title,
            "description": self.description,
            "media source": self.media_source,
            # do not serialize the password, its a security breach
            "post date": self.post_date
        }

class TypesOfPosts(Base):
    __tablename__ = 'TypesOfPosts'
    type_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Posts.post_id'), nullable=False)
    type_of = Column(String, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title

    def serialize(self):
        return {
            "type id": self.type_id,
            "post id": self.post_id,
            "user id": self.user_id,
        }

class Likes(Base):
    __tablename__ = "Likes"
    like_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Posts.post_id'), nullable=False)
    like_value = Column(Boolean, nullable=False)
    like_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)

    def __repr__(self):
        return '<Like %r>' % self.like_value

    def serialize(self):
        return {
            "like id": self.like_id,
            "post id": self.post_id,
            "like value": self.like_value,
            # do not serialize the password, its a security breach
            "like date": self.like_date,
            "user id": self.user_id
        }

class Comments(Base):
    __tablename__ = 'Comments'
    comment_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Posts.post_id'), nullable=False)
    comment_value = Column(String, nullable=False)
    comment_date = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)

    def __repr__(self):
        return '<Comment %r>' % self.comment_value

    def serialize(self):
        return {
            "comment id": self.comment_id,
            "post id": self.post_id,
            "comment value": self.comment_value,
            # do not serialize the password, its a security breach
            "comment date": self.comment_date,
            "user id": self.user_id
        }

class Followers(Base):
    __tablename__ = 'Followers'
    follower_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)

    def __repr__(self):
        return '<Follower %r>' % self.like_value

    def serialize(self):
        return {
            "user id": self.user_id
        }




    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e