#!/usr/bin/python3
"""This module define the BusinessUser Class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class BusinessUser(BaseModel, Base, UserMixin):
    """This class defines a BusinessUser"""
    __tablename__ = 'business_users'

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    profile_pic = Column(String(20), nullable=False, default='default.jpg')
    password_hash = Column(String(162), nullable=False)

    businesses = relationship('Business', backref='owner',
                              cascade='all, delete, delete-orphan')

    def __init__(self, *args, **kwargs):
        """Initializes BusinessUser"""
        if 'password' in kwargs:
            self.password_hash = generate_password_hash(kwargs.pop('password'))
        super().__init__(*args, **kwargs)

    def verify_password(self, password):
        """Verify BusinessUser password"""
        return check_password_hash(self.password_hash, password)
