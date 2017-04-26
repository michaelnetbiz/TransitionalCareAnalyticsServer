# -*- coding: utf-8 -*-
"""The application's administration blueprint.

Provides models and helper functions for application administration. Implements the views for client to administer 
application. 

Attributes
----------
mod_admin : flask.blueprints.Blueprint

"""
# TODO: implement logic returning number of sessions that coincide with home visits versus number that don't
# TODO: add methods for descriptive statistics on system state, status, contents

from flask import Blueprint

from tcas.helper.blueprint_router_mixin import token_level_view_args, type_level_view_args
from tcas.helper.url_getter import url_getter
from tcas.helper.endpoint_getter import endpoint_getter
from .view import *

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')

report_endpoint = endpoint_getter(ReportView)
report_url = url_getter(ReportView)
report_converter = 'string'
report_key = '_name'
report_view_func = ReportView.as_view(report_endpoint)
mod_admin.add_url_rule(
    report_url,
    defaults=type_level_view_args,
    view_func=report_view_func,
    methods=['GET']
)
mod_admin.add_url_rule(
    '%s<%s:%s>' % (report_url, report_converter, report_key),
    view_func=report_view_func,
    methods=['GET']
)

upload_endpoint = endpoint_getter(UploadView)
upload_url = url_getter(UploadView)
upload_converter = UploadView.converter
upload_key = UploadView.key
upload_view_func = UploadView.as_view(upload_endpoint)
mod_admin.add_url_rule(
    upload_url,
    defaults=token_level_view_args,
    view_func=upload_view_func,
    methods=['GET']
)
mod_admin.add_url_rule(
    upload_url,
    view_func=upload_view_func,
    methods=['POST']
)
mod_admin.add_url_rule(
    '%s<%s:%s>' % (upload_url, upload_converter, upload_key),
    view_func=upload_view_func,
    methods=['GET', 'DELETE']
)


@mod_admin.route('/reporting')
def run_reporting_task():
    """Run reporting task asynchronously.
    """
    pass
