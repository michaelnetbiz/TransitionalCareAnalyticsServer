# -*- coding: utf-8 -*-
"""The application's administration blueprint. Provides models and helper functions for application administration.
Implements the views for client to administer application.

Attributes
----------
mod_admin : flask.blueprints.Blueprint

"""
# TODO: implement logic returning number of sessions that coincide with home visits versus number that don't
# TODO: add methods for descriptive statistics on system state, status, contents
from flask import Blueprint
from tcas.helper.blueprint_router_mixin import token_level_view_args, type_level_view_args
from tcas.admin.view.report_view import ReportView
from tcas.admin.view.task_view import TaskView
from tcas.admin.view.upload_view import UploadView
from tcas.admin.view.report_view import report_converter, report_endpoint, report_key, report_url, report_view_func
from tcas.admin.view.task_view import task_converter, task_endpoint, task_key, task_url, task_view_func
from tcas.admin.view.upload_view import upload_converter, upload_endpoint, upload_key, upload_url, upload_view_func

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')

mod_admin.add_url_rule(report_url, defaults=type_level_view_args, view_func=report_view_func, methods=['GET'])
mod_admin.add_url_rule(upload_url, defaults=token_level_view_args, view_func=upload_view_func, methods=['GET'])
mod_admin.add_url_rule(upload_url, view_func=upload_view_func, methods=['POST'])

mod_admin.add_url_rule(
    '%s<%s:%s>' % (report_url, report_converter, report_key),
    view_func=report_view_func,
    methods=['GET']
)

mod_admin.add_url_rule(
    '%s<%s:%s>' % (task_url, task_converter, task_key),
    view_func=task_view_func,
    methods=['GET']
)

mod_admin.add_url_rule(
    '%s<%s:%s>' % (upload_url, upload_converter, upload_key),
    view_func=upload_view_func,
    methods=['GET', 'DELETE']
)
