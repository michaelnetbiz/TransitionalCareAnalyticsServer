# -*- coding: utf-8 -*-
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from tcas.db import Base, CommonMixin


class GoalStepType(CommonMixin, Base):
    # declare relationships
    goal_steps = relationship('GoalStep')

    # declare foreign keys

    # declare attributes
    name = Column(String())
