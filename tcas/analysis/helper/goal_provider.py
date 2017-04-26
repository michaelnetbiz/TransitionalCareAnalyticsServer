# -*- coding: utf-8 -*-
from pandas import read_csv


def goal_provider(goals_in_csv, goals_out_csv):
    """Provide DataFrames of goals from .csv files.
    
    Parameters
    ----------
    goals_in_csv : str
        File path of the .csv file containing input data from which to provide goals.
        
    goals_out_csv : str
        File path of the .csv file containing data that goal abstraction should be able to reproduce.

    Returns
    -------
    goals : tuple of pandas.DataFrame
        Tuple of DataFrames. First DataFrame contains input data. Second DataFrame contains output data.
        
    """
    columns = [
        'ba_goal1',
        'ba_goal2',
        'ba_goal3',
        'ba_goal4',
        'ba_goal5',
        'ba_goal6',
        'co_goalsmet',
        'sp_goal1',
        'sp_goal2',
        'sp_goal3',
        'sp_goal4',
        'sp_goal5',
        'sp_goal6',
        'sp_goal7',
        'sp_goal8',
        'sp_goal9',
        'sp_goal10',
        'sp_goal11',
        'sp_goal12',
        'sp_goal13',
        'sp_goal14',
        'sp_goal15'
    ]
    goals_in = read_csv(goals_in_csv, encoding='iso8859-2', na_values=['nan', ''])[columns]
    goals_out = read_csv(goals_out_csv)
    goals = (goals_in, goals_out)
    return goals
