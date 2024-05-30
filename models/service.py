#!/usr/bin/python3
"""This module defines the Service class"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class Service(BaseModel, Base):
    """Represents a service offered by a business"""
    __tablename__ = 'services'

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    business_id = Column(String(60), ForeignKey('businesses.id'),
                         nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes Service"""
        super().__init__(*args, **kwargs)
