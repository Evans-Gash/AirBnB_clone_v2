#!/usr/bin/python3
"""
Module containing the Amenity class.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity
import os


class Amenity(BaseModel, Base):
    """
    Amenity class to store information about amenities.
    """

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        'Place', secondary=place_amenity, back_populates='amenities')
