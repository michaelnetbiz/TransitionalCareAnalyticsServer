from itsdangerous import Serializer, SignatureExpired, BadSignature
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

from tcas.config import SECRET_KEY
from tcas.db import Base, CommonMixin


class User(UserMixin, CommonMixin, Base):
    public_attributes = ['email']
    # declare relationships
    uploads = relationship('Upload')

    # declare foreign keys

    # declare attributes
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    @declared_attr
    def __mutable__(self):
        return ['email']

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.uploads = []

    @property
    def password(self):
        raise AttributeError('Getting password attribute disallowed')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def authenticate(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def validate_post_data(data):
        if 'email' in data.keys() and 'password' in data.keys():
            return data
        else:
            return None

    @staticmethod
    def validate_put_data(data):
        if 'password' in data.keys():
            return data
        else:
            return None

    @staticmethod
    def validate_delete_data(data):
        if 'password' in data.keys():
            return data
        else:
            return None

    def serialize(self):
        return {
            'date_created': self.date_created.__str__(),
            'email': self.email
        }

    def generate_token(self):
        s = Serializer(SECRET_KEY)
        return s.dumps({'id': self.id})
