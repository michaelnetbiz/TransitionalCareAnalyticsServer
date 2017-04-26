# -*- coding: utf-8 -*-
"""The application's authentication blueprint.

Provides models and helper functions for managing authentication. Implements views for client to authenticate.

Attributes
----------
mod_auth : flask.blueprints.Blueprint
token_level_view_args : dict
type_level_view_args : dict

"""

from flask import Blueprint

from tcas.helper.url_getter import url_getter
from tcas.helper.endpoint_getter import endpoint_getter
from .view import *

token_level_view_args = {'_id': None}
type_level_view_args = {'_name': None}

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

auth_endpoint = endpoint_getter(AuthView)
user_endpoint = endpoint_getter(UserView)
auth_url = '/'
user_url = url_getter(UserView)
user_converter = UserView.converter
user_key = UserView.key
auth_view_func = AuthView.as_view(auth_endpoint)
user_view_func = UserView.as_view(user_endpoint)

mod_auth.add_url_rule(
    user_url,
    defaults=token_level_view_args,
    view_func=user_view_func,
    methods=['GET']
)
mod_auth.add_url_rule(
    user_url,
    view_func=user_view_func,
    methods=['POST']
)
mod_auth.add_url_rule(
    '%s<%s:%s>' % (user_url, user_converter, user_key),
    view_func=user_view_func,
    methods=['GET', 'UPDATE', 'DELETE']
)
mod_auth.add_url_rule(
    auth_url,
    view_func=auth_view_func,
    methods=['POST']
)
