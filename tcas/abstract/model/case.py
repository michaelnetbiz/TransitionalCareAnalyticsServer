# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy.orm import relationship

from tcas.abstract.model.condition_enum import ConditionEnum
from tcas.db import Base, CommonMixin


class Case(CommonMixin, Base):
    """Represent a patient-caregiver dyad."""

    def __init__(self, record_id, condition, goals):
        """Case instance constructor.

        Parameters
        ----------
        record_id : str
        condition : str
        goals : str
        """
        self.condition = condition
        self.goals = goals
        self.record_id = record_id

    condition = sqlalchemy.Column(sqlalchemy.Enum(ConditionEnum))
    goals = relationship('Goal')
    record_id = sqlalchemy.Column(sqlalchemy.String(), unique=True)
