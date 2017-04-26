# -*- coding: utf-8 -*-
"""The application's analysis blueprint.

Provides models, helper functions, and views for analysis domain entities.

Attributes
----------
mod_analysis : flask.blueprints.Blueprint

"""
from flask import Blueprint, redirect, url_for
from tcas.analysis.task import cluster_goals

mod_analysis = Blueprint('analysis', __name__, url_prefix='/analysis')


@mod_analysis.route('/goal/clustering/')
def run_goal_clustering_task():
    """Run clustering task asynchronously

    Returns
    -------

    """
    async_task = cluster_goals.apply_async()
    return redirect(url_for('analysis.get_goal_clustering_task_status', task_id=async_task.id))


@mod_analysis.route('/goal/clustering/status/<task_id>/')
def get_goal_clustering_task_status(task_id):
    """Get a status for a given task.

    Parameters
    ----------
    task_id

    Returns
    -------

    """
    async_task = cluster_goals.AsyncResult(task_id)
    return async_task.state
