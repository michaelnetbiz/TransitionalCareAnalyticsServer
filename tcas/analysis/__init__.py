# -*- coding: utf-8 -*-
"""The application's analysis blueprint. Provides models, helper functions, and views for analysis domain entities.

Attributes
----------
mod_analysis : flask.blueprints.Blueprint

"""
from flask import Blueprint
from tcas.analysis.view.clustering_view import clustering_endpoint
from tcas.analysis.view.clustering_view import clustering_url
from tcas.analysis.view.clustering_view import clustering_converter
from tcas.analysis.view.clustering_view import clustering_key
from tcas.analysis.view.clustering_view import clustering_view_func

mod_analysis = Blueprint('analysis', __name__, url_prefix='/analysis')

mod_analysis.add_url_rule(clustering_url, view_func=clustering_view_func, methods=['GET'])
