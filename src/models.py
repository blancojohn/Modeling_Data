import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorites_table = Table(
    'favorites',
    Base.metadata,
    Column('favorite_id', Integer, ForeignKey('users.id'), nullable=False, primary_key=True),
    Column('item_favorite_id', Integer, ForeignKey('users.id'), nullable=False, primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    loginStatus = Column(String(250), default=True) #Show messague de Start session.
    email = Column(String (250), nullable=False)

    #Many to many relationship. A user can have on the table many favorites planets or characters and the favorites table can have many users. 
    
    favorites = relationship(
        'User',
        secondary= favorites_table,
        primaryjoin= (favorites_table.c.favorite_id == id),
        secondaryjoin= (favorites_table.c.item_favorite_id == id),
        backref= backref('items_favorites_id', lazy= 'dynamic')
    )

class Planet(Base):
    #One to many. One planet can have many users
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='planets')

class Character(Base):
    #One to many. One Character can have many users
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Age = Column(String(250), nullable=True)
    vehicle = Column(String(250), nullable=True)
    starships = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='characters')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


    


 
