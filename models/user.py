#!/usr/bin/python3
<<<<<<< HEAD
"""This is the user class."""
from models.base_model import BaseModel, Base
=======
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    reviews = relationship('Review', backref='user',
                           cascade='delete')
    places = relationship('Place', backref='user',
                          cascade='delete')
=======
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
