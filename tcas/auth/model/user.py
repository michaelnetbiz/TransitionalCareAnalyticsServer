# -*- coding: utf-8 -*-
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from tcas.config import SECRET_KEY
from tcas.db import Base, CommonMixin


class User(UserMixin, CommonMixin, Base):
    """Represents Users of the application
    """
    public_attributes = ['email']
    uploads = relationship('Upload')
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    @declared_attr
    def __mutable__(self):
        return ['email']

    def is_authenticated(self):
        """Instance method returns whether or not the User instance is authenticated.
        Returns
        -------
        bool
        """
        return True

    def is_active(self):
        """Instance method returns whether or not the User instance is active.
        Returns
        -------
        bool
        """
        return True

    def is_anonymous(self):
        """Instance method returns whether or not the User instance is anonymous.
        Returns
        -------
        bool
        """
        return False

    def get_id(self):
        """Instance method returns User identifier.
        Returns
        -------
        str
        """
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

    @staticmethod
    def verify_credentials(email, password):
        """Verifies combination of User email and User password.
        Parameters
        ----------
        email : str
        password : str

        Returns
        -------
        bool
        """
        user = User.query.filter_by(email=email).first()
        if not user:
            return False
        return check_password_hash(user.password_hash, password)

    @staticmethod
    def validate_post_data(data):
        """Validates the contents of POST requests.

        Parameters
        ----------
        data

        Returns
        -------

        """
        if not data:
            return
        elif 'email' in data.keys() and 'password' in data.keys():
            return data
        else:
            return

    @staticmethod
    def validate_put_data(data):
        if 'password' in data.keys():
            return data
        else:
            return

    @staticmethod
    def validate_delete_data(data):
        if 'password' in data.keys():
            return data
        else:
            return

    def serialize(self):
        return {
            'date_created': self.date_created.__str__(),
            'email': self.email
        }

    def generate_token(self):
        """Generates authentication token.

        Returns
        -------
        str

        """
        serializer = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=300)
        return serializer.dumps({'id': self.id})

    @staticmethod
    def verify_token(token):
        """Verifies provided authentication token.

        Parameters
        ----------
        token

        Returns
        -------
        tcas.auth.model.user.User

        """
        serializer = TimedJSONWebSignatureSerializer(SECRET_KEY)
        try:
            _id = serializer.loads(token)
        except SignatureExpired:
            return
        except BadSignature:
            return
        return User.query.filter_by(id=_id).first()
