# -*- coding: utf-8 -*-
import re
import nltk
import sqlalchemy
import sqlalchemy.orm as orm
import sqlalchemy.sql as sql
import sqlalchemy.dialects as dialects

from tcas.db import Base
from tcas.db import CommonMixin
from tcas.db import database_session as session
from tcas.abstract.model.goal_step import GoalStep
from tcas.abstract.model.goal_source_enum import GoalSourceEnum


class Goal(CommonMixin, Base):
    """Represent patient/caregiver goal.
    """
    PROPER_NOUNS_AND_PRONOUNS = [
        'caregiver',
        'cg',
        'client',
        'he',
        'i',
        'mr',
        'mrs',
        'ms',
        'patient',
        'pt',
        'ptcg',
        'she',
        'scwm',
        'swcm'
    ]

    NUMERIC_PATTERN = re.compile(
        '\#[0-9]|[0-9][),\.]|[0-9A-Z]{4,5}[\.)-]|[A-Z]{4}\s[A-Z]{1,5}\:|[GgOoAaLl][0-9][:,\s]'
    )

    @staticmethod
    def goal_step_extractor():
        """Decompose goal instances into goal-steps.
        """
        s = session()
        goals = Goal.query.all()
        for goal in goals:
            print(goal.old_numbered, type(goal.old_numbered))
            for each in goal.old_numbered:
                gs = GoalStep(each, goal.id)
                s.add(gs)
                s.commit()

    @staticmethod
    def handle_proper_nouns(data):
        """
        Parameters
        ----------
        data
        """
        rv = []
        tokens = nltk.word_tokenize(data)
        for token in tokens:
            if token.lower().replace('.', '').replace('/', '') in Goal.PROPER_NOUNS_AND_PRONOUNS:
                rv.append(token.capitalize())
            else:
                rv.append(token.lower())
        return rv

    # primary key, discriminator, and class attributes
    discriminator = sqlalchemy.Column(sqlalchemy.String(2))

    # relationships
    steps = orm.relationship('GoalStep')

    # is-a relationships

    # attr
    source = sqlalchemy.Column(sqlalchemy.Enum(GoalSourceEnum))
    unaltered_text = sqlalchemy.Column(sqlalchemy.Text, index=True)

    explanations = sqlalchemy.Column(dialects.postgresql.ARRAY(sqlalchemy.Text))
    quotations = sqlalchemy.Column(dialects.postgresql.ARRAY(sqlalchemy.Text))
    numbered = sqlalchemy.Column(dialects.postgresql.ARRAY(sqlalchemy.Text))
    old_numbered = sqlalchemy.Column(dialects.postgresql.ARRAY(sqlalchemy.Text))
    another_numbered = sqlalchemy.Column(dialects.postgresql.ARRAY(sqlalchemy.Text))
    tokens = sqlalchemy.Column(dialects.postgresql.ARRAY(sqlalchemy.Text))
    parts_of_speech = sqlalchemy.Column(dialects.postgresql.ARRAY(sqlalchemy.Text))
    punkt_tokenized = sqlalchemy.Column(dialects.postgresql.ARRAY(sqlalchemy.Text))
    diff = sqlalchemy.Column(sqlalchemy.Text)

    # foreign keys
    # service_plan = sqlalchemy.Column(sqlalchemy.String(16), sqlalchemy.ForeignKey('interaction.id'))

    # arguments to enable class polymorphic inheritance from Interaction
    goal_type = orm.column_property(sql.expression.case([
        (discriminator == 'FG', 'financial_goal'),
        (discriminator == 'SS', 'social_support_goal'),
        (discriminator == 'MG', 'medical_goal')
    ], else_='goal'))

    __mapper_args__ = {
        'polymorphic_identity': 'goal',
        'polymorphic_on': goal_type
    }

    # constructor
    def __init__(self, data, source):
        """Goal constructor method.
        Parameters
        ----------
        data : str
        source : str
        """
        self.source = source
        self.unaltered_text = data

        self.explanations = nltk.regexp_tokenize(self.unaltered_text, pattern='\([A-Za-z0-9\s\.\/\%\-]{0,}\)')
        self.quotations = nltk.regexp_tokenize(self.unaltered_text, pattern='\'[A-Za-z0-9\s\.\/\%\-]{0,}\'')
        self.numbered = nltk.regexp_tokenize(self.unaltered_text, pattern='[0-9\.\)]')
        self.old_numbered = [
            s for s in Goal.NUMERIC_PATTERN.split(self.unaltered_text)
            if len(s) > 3 and s.isnumeric() is False
        ]
        self.another_numbered = nltk.regexp_tokenize(
            self.unaltered_text,
            pattern='[0-9\)\.]'
        )
        self.tokens = Goal.handle_proper_nouns(self.unaltered_text)
        self.parts_of_speech = nltk.pos_tag(self.tokens)

        diff1 = ''.join(
            [
                self.unaltered_text.replace(explanation, '')
                for explanation in self.explanations
            ]
        )
        diff2 = ''.join(
            [
                diff1.replace(quotation, '')
                for quotation in self.quotations
            ]
        )
        self.diff = diff2


class FinancialGoal(Goal):
    # set arguments to enable class polymorphic inheritance from Interaction
    __mapper_args__ = {
        'polymorphic_identity': 'financial_goal',
    }

    # declare relationships

    # declare foreign keys
    id = sqlalchemy.Column(sqlalchemy.String(16), sqlalchemy.ForeignKey('goal.id'), primary_key=True)

    # declare own attributes


class SocialSupportGoal(Goal):
    # set arguments to enable class polymorphic inheritance from Interaction
    __mapper_args__ = {
        'polymorphic_identity': 'social_support_goal',
    }

    # declare relationships

    # declare foreign keys
    id = sqlalchemy.Column(sqlalchemy.String(16), sqlalchemy.ForeignKey('goal.id'), primary_key=True)

    # declare own attributes


class MedicalGoal(Goal):
    # set arguments to enable class polymorphic inheritance from Interaction
    __mapper_args__ = {
        'polymorphic_identity': 'medical_goal',
    }

    # declare relationships

    # declare foreign keys
    id = sqlalchemy.Column(sqlalchemy.String(16), sqlalchemy.ForeignKey('goal.id'), primary_key=True)

    # declare own attributes
