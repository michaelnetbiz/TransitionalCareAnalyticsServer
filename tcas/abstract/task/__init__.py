# -*- coding: utf-8 -*-
from tcas.config import MASTER_CSV, GOALS_OUT
from tcas.task_manager import task_manager
from tcas.analysis.helper.goal_provider import goal_provider
from tcas.analysis.helper.series_helpers import goal_abstractor


@task_manager.task()
def abstract_goals(goal_abstractee):
    """Run abstraction task

    Parameters
    ----------
    goal_abstractee

    Returns
    -------
    app.casework.model.goal.Goal
    """
    # TODO: check performance of RegexpTokenizer v. WhitespaceTokenizer with str.startswith('\''), str.startswith('(')
    # TODO: test against contractions.csv?

    goals_in, test_goals_out = goal_provider(
        MASTER_CSV,
        GOALS_OUT
    )

    goals_in.apply(goal_abstractor, axis=0)


@task_manager.task()
def abstract_cases(case_abstractee):
    """

    Parameters
    ----------
    case_abstractee

    Returns
    -------
    app.casework.model.case.Case

    """

    # rand_arm_assignment is the source of case condition attribute
    return case_abstractee
