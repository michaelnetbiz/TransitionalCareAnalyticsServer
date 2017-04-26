# -*- coding: utf-8 -*-
import sqlalchemy

from tcas.db import Base, CommonMixin


class GoalStep(CommonMixin, Base):
    """Represent Goal component.

    """
    # declare relationships

    # declare foreign keys
    goal = sqlalchemy.Column(sqlalchemy.String(16), sqlalchemy.ForeignKey('goal.id'))
    goal_step_type = sqlalchemy.Column(sqlalchemy.String(16), sqlalchemy.ForeignKey('goal_step_type.id'))

    # declare attributes
    content = sqlalchemy.Column(sqlalchemy.Text)

    def __init__(self, content, goal):
        self.content = content
        self.goal = goal
