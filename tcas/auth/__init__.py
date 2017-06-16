# -*- coding: utf-8 -*-
"""The application's authentication blueprint. Provides models and helper functions for managing authentication.
Implements views for client to authenticate.

Attributes
----------
mod_auth : flask.blueprints.Blueprint

"""
from flask import Blueprint
from tcas.helper.blueprint_router_mixin import token_level_view_args
from tcas.auth.view.auth_view import AuthView
from tcas.auth.view.auth_view import auth_endpoint, auth_url, auth_view_func
from tcas.auth.view.user_view import UserView
from tcas.auth.view.user_view import user_converter, user_endpoint, user_key, user_url, user_view_func

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

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
    methods=['GET', 'POST']
)
