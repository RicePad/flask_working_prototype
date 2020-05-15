import sys

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, Enum

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


# create declarative_base instance
Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_Name = Column(String(25), nullable=False)
    last_Name = Column(String(25), nullable=False)
    # designation = relationship('Club')
    student_ID = Column(Integer, unique=True, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(50), unique=True)
    gender = Column(Boolean)
    comments = Column(Text)

    def __repr__(self):
        return '<User %r' % self.first_Name


# we create the class Book and extend it from the Base Class.
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///books-collection.db')

Base.metadata.create_all(engine)
