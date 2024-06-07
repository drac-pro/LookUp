#!/usr/bin/python3
"""Define DBStorage class"""
from os import getenv
from models.base_model import Base
from models.business_user import BusinessUser
from models.business import Business
from models.service import Service
from models.location import Location
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


classes = [BusinessUser, Business, Service, Location]


class DBStorage:
    """Creates connection with mysql database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage"""
        user = getenv('LOOKUP_MYSQL_USER')
        passwd = getenv('LOOKUP_MYSQL_PWD')
        host = getenv('LOOKUP_MYSQL_HOST')
        db = getenv('LOOKUP_MYSQL_DB')
        env = getenv('LOOKUP_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
           user, passwd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a class"""
        result = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for cls in classes:
                objs.extend(self.__session.query(cls).all())
        for obj in objs:
            key = obj.__class__.__name__ + '.' + obj.id
            result[key] = obj
        return result

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """closes the current session by calling remove on it"""
        self.__session.close()

    def get_user_by_email(self, email):
        """Get a user by their email"""
        return self.__session.query(BusinessUser).\
            filter_by(email=email).one_or_none()

    def get_user_by_id(self, user_id):
        return self.__session.query(BusinessUser).get(user_id)

    def get_service(self, business_id):
        return self.__session.query(Service).\
            filter_by(business_id=business_id).first()

    def get(self, cls, id):
        """retrieve one object based on the class and id

        Args:
            cls: Class of object
            id: object id

        Returns:
            The object if found, otherwise None
        """
        if cls not in classes:
            return None
        return self.__session.query(cls).get(id)

    def count(self, cls=None):
        """count the number of objects in storage"""
        if cls and cls in classes:
            return len(self.all(cls))
        else:
            return len(self.all())
