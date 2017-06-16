# -*- coding: utf-8 -*-
"""The application's task manager. Provides a celery instance and discovers tasks from the application's component
packages.

Attributes
----------
task_manager : flask.blueprints.Blueprint

"""
from celery import Celery
from tcas.config import TASK_BACKEND, TASK_BROKER

task_manager = Celery(
    backend=TASK_BACKEND,
    broker=TASK_BROKER
)

task_manager.autodiscover_tasks(
    packages=['tcas.abstract', 'tcas.admin', 'tcas.analysis', 'tcas.auth'],
    related_name='task'
)
