# -*- coding: utf-8 -*-
import inflection
from random import choice
from sqlalchemy import create_engine, Column, DateTime, func, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from tcas.config import DATABASE_URI

engine = create_engine(DATABASE_URI, convert_unicode=True)
database_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = database_session.query_property()


def initialize_model(eng=engine):
    """Initializes data model.

    Parameters
    ----------
    eng

    """
    Base.metadata.create_all(bind=eng)


def reset_model(eng=engine):
    """Resets data model.

    Parameters
    ----------
    eng

    """
    Base.metadata.drop_all(bind=eng)


def model_uri_generator():
    """Generates uri.

    Returns
    -------
    str

    Example usage:

    >>> print(model_uri_generator()) #random
    fe8329ab02fd6451

    """
    return ''.join(choice('0123456789abcdef') for i in range(16))


class CommonMixin(object):
    """Provides common data model attributes.

    Attributes
    ----------
    id : sqlalchemy.String
    date_created : sqlalchemy.DateTime
    date_updated : sqlalchemy.DateTime
    public_attributes : list

    """
    public_attributes = []

    @declared_attr
    def __tablename__(self):
        return inflection.underscore(self.__name__)

    id = Column(String(16), primary_key=True, default=model_uri_generator)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())
