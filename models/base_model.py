#!/usr/bin/python3
"""Defines a Class base_model which will be inherited by other classes"""
import models
import uuid
from datatime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

time = '%Y-%m-%dT%H:%M:%S.%f'

Base = declarative_base()


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datatime.utcnow)
    updated_at = Column(DateTime, default=datatime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datatime.strptime(kwargs['created_at'], time)
            else:
                self.created_at = datatime.utcnow()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datatime.strptime(kwargs['updated_at'], time)
            else:
                self.updated_at = datatime.utcnow()
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datatime.utcnow()

    def __str__(self):
        """String representation of the BaseModel class"""
        return '[{:s}] ({:s}) {}'.format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """save changes to made to an object"""
        self.updated_at = datetime.utcnow()
        self.storage.new(self)
        self.storage.save()

    def to_dict(self, save_fs=None):
        """return the dictionary of the object"""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """deletes object from the storage"""
        models.storage.delete()
