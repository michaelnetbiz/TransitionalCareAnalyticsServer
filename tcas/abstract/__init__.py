# -*- coding: utf-8 -*-
"""The application's abstraction blueprint. Provides models, helper functions, and views for abstracting domain
entities from data.

Attributes
----------
mod_abstract : flask.blueprints.Blueprint

"""
# TODO: add methods for summary statistics on variables like computer self-efficacy, gender, race, etc.
from flask import Blueprint
from tcas.helper.blueprint_router_mixin import token_level_view_args, type_level_view_args
from tcas.abstract.view.case_view import case_converter, case_key, case_view_func, case_url
from tcas.abstract.view.goal_view import goal_converter, goal_key, goal_view_func, goal_url

mod_abstract = Blueprint('abstract', __name__, url_prefix='/abstract')

mod_abstract.add_url_rule(
    case_url,
    defaults=token_level_view_args,
    view_func=case_view_func,
    methods=['GET']
)
mod_abstract.add_url_rule(
    case_url,
    view_func=case_view_func,
    methods=['POST']
)
mod_abstract.add_url_rule(
    '%s<%s:%s>' % (case_url, case_converter, case_key),
    view_func=case_view_func,
    methods=['GET', 'PUT', 'DELETE']
)

mod_abstract.add_url_rule(
    goal_url,
    defaults=token_level_view_args,
    view_func=goal_view_func,
    methods=['GET']
)
mod_abstract.add_url_rule(
    goal_url,
    view_func=goal_view_func,
    methods=['POST']
)
mod_abstract.add_url_rule(
    '%s<%s:%s>' % (goal_url, goal_converter, goal_key),
    view_func=goal_view_func,
    methods=['GET', 'PUT', 'DELETE']
)
