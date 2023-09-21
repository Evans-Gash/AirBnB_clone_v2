#!/usr/bin/python3
"""This is the user module for our application."""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.base_model import BaseModel
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """User class for representing user information."""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
