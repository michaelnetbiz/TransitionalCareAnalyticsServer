# -*- coding: utf-8 -*-
"""Factory function for initializing the application.

"""
from flask import Flask, jsonify


def create_tcas(conf=None):
    """

    Parameters
    ----------
    conf

    Returns
    -------

    """
    from tcas.abstract import mod_abstract
    from tcas.admin import mod_admin
    from tcas.analysis import mod_analysis
    from tcas.auth import mod_auth

    from tcas.admin.model import Page, Pageview, Upload
    from tcas.auth.model import User
    from tcas.abstract.model.case import Case
    from tcas.abstract.model.goal import Goal, FinancialGoal, MedicalGoal, SocialSupportGoal
    from tcas.abstract.model.goal_step import GoalStep
    from tcas.abstract.model.goal_step_type import GoalStepType
    from tcas.db import database_session, initialize_model
    from tcas.auth.helper import login_manager
    from tcas.config import APP_DIR

    application = Flask(__name__)
    application.config.from_envvar('TCAS_SETTINGS')
    initialize_model()
    application.register_blueprint(mod_abstract)
    application.register_blueprint(mod_admin)
    application.register_blueprint(mod_analysis)
    application.register_blueprint(mod_auth)

    login_manager.init_app(application)

    application.add_url_rule('/', 'index', lambda: jsonify(sorted([str(r) for r in app.url_map.iter_rules()])))

    @application.teardown_appcontext
    def shutdown_session(e):
        """Shut down session

        Parameters
        ----------
        e : Exception
        """
        database_session.remove()

    return application
