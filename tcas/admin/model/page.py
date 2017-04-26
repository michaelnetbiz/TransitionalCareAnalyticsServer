from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from tcas.db import Base, CommonMixin


class Page(CommonMixin, Base):
    # declare relationships
    pageviews = relationship('Pageview')

    # declare foreign keys

    # declare attributes
    uri = Column(String)
