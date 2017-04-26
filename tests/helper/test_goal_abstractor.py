# -*- coding: utf-8 -*-
from tcas.config import GOALS_OUT, MASTER_CSV
from tcas.analysis.helper.series_helpers import goal_abstractor
from tcas.analysis.helper.goal_provider import goal_provider


def test_goal_abstractor():
    """Test Goal abstraction.

    """
    goals_in, test_goals_out = goal_provider(
        MASTER_CSV,
        GOALS_OUT
    )
    # goals_in.apply(goal_abstractor, ())
    ba_goal1 = goals_in.ba_goal1.dropna().to_dict()
    for g in ba_goal1.items():
        k = g[0]
        v = g[1]
        print(v)
    # assert goal_abstractor(goals_in) == test_goals_out
