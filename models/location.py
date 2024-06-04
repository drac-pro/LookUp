#!/usr/bin/python3
"""This module define the Location Class"""
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Location(BaseModel, Base):
    """Represents the Location of a Business"""
    __tablename__ = 'locations'

    address = Column(String(256), nullable=False)
    city = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    country = Column(String(128), nullable=False)
    zip_code = Column(String(20), nullable=False)

    businesses = relationship('Business', backref='location',
                              cascade='all, delete, delete-orphan')

    def __init__(self, *args, **kwargs):
        """Initializes Location"""
        super().__init__(*args, **kwargs)
