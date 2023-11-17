import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    loginStatus = Column(String(250), default=True) #Show messague de Start session.
    email = Column(String (250), nullable=False)


    

class Planet(Base):
    #One to many. One planet can have many users
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)

class Character(Base):
    #One to many. One Character can have many users
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Age = Column(String(250), nullable=True)
    vehicle = Column(String(250), nullable=True)
    starships = Column(String(250), nullable=True)

class Favorite_planet(Base):
    #One to many. One Character can have many users
    __tablename__= 'favorites_planets'
    id = Column(Integer, primary_key=True)
    name_planet= Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='favorites_planets')
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    planet = relationship('Planet', backref='favorites_planets')


class Favorite_character(Base):
    #One to many. One Character can have many users
    __tablename__= 'favorites_characters'
    id = Column(Integer, primary_key=True)
    name_planet= Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='favorites_characters')
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    character = relationship('Character', backref='favorites_characters')








    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


    


 
