import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False, unique=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    email = Column(String(25), nullable=False, unique=True)
    active = Column(Boolean, default=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    status = Column(Boolean, default=True)
    species = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class Character_user(Base):
    __tablename__ = 'character_user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)
   
class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    type = Column(String(250), nullable=False)
    dimension = Column(String(250), nullable=False)

class Location_user(Base):
    __tablename__ = 'location_user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship(Locations)

class Episodes(Base):
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    air_date = Column(String(250), nullable=False)
    episode = Column(String(250), nullable=False)

class Episode_user(Base):
    __tablename__ = 'episode_user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    episode_id = Column(Integer, ForeignKey('episodes.id'))
    episode = relationship(Episodes)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship(Locations)
    episode_id = Column(Integer, ForeignKey('episodes.id'))
    episode = relationship(Episodes)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
