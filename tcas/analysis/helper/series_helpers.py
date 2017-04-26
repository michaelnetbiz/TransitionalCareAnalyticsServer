# -*- coding: utf-8 -*-
import nltk

from tcas.config import ENGLISH_PICKLE
from tcas.db import database_session as session
from tcas.abstract.model.goal_step import GoalStep
from tcas.abstract.model.goal import Goal

s = session()
detector = nltk.data.load(ENGLISH_PICKLE)


def process(data, cls, source):
    """
    Parameters
    ----------
    cls : sqlalchemy.ext.declarative.api.DeclarativeMeta
    data : str
    source : str
    Returns
    -------
    """
    goal_sentences = detector.tokenize(data)
    for sentence in goal_sentences:
        instance = cls(sentence, source)
        s.add(instance)
    s.commit()


def goal_abstractor(goal_series):
    """Abstract goals from pandas.Series objects.
    
    Parameters
    ----------
    goal_series : pandas.core.series.Series
        Series from which to abstract GoalStatements.

    Returns
    -------
    """
    source = goal_series.name
    # [y.lower() for y in x if x not in PROPER_NOUNS_AND_PRONOUNS
    goal_series.dropna().apply(process, args=(Goal, source))
