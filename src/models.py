import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

planets_favorites_table = Table(
    'planets_favorites_table',
    Base.metadata,
    Column('planet_favorite_id', Integer, ForeignKey('users_id'), nullable=False, primary_key=True),
    Column('user_palnet_id', Integer, ForeignKey('users_id'), nullable=False, primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    usuarname = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False )
    email = Column(String (250), nullable=False)
    
    planets_favorites = relationship(
        'User',
        secondary=planets_favorites,
        primaryjoin= (planets_favorites_table.c.planet_favorite_id == id),
        secundaryjoin= (planets_favorites_table.c.user_planet_id == id),
        backref= backref('users_planets_id', lazy= 'dynamic')
    )
    

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nulllable=False)
    period_rotation = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(259))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship()

class People(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key=True)
    name = Column(String,(250), nulllable=False)
    Starship = Column(String,(250))
    birth_year = Column(String,(250))

 
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
