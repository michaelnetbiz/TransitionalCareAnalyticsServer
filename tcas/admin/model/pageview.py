from sqlalchemy import Column, ForeignKey, Integer, String

from tcas.db import Base, CommonMixin


class Pageview(CommonMixin, Base):
    # TODO: relate pageviews and interactions (time dimension)
    # TODO: relate pageviews to patient/caregiver variables (e.g., computer self-efficacy)

    # declare relationships

    # declare foreign keys
    case = Column(String(16), ForeignKey('case.id'))
    page = Column(String(16), ForeignKey('page.id'))

    # declare attributes
    timestamp = Column(Integer)
