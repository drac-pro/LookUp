#!/usr/bin/python3
"""This module define the Business Class"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Business(BaseModel, Base):
    """Defines a Business"""
    __tablename__ = 'businesses'

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    business_user_id = Column(String(60), ForeignKey('business_user.id'),
                              nullable=False)
    location_id = Column(String(60), ForeignKey('locations.id'),
                         nullable=False)
    services = relationship('Service', backref='business',
                            cascade='all, delete, delete-orphan')

    def __init__(self, *args, **kwargs):
        """Initializes Business"""
        super().__init__(*args, **kwargs)
