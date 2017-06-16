# -*- coding: utf-8 -*-
"""The application's core module, containing a factory function for its initialization.
"""
from flask import Flask, g, jsonify, make_response
from flask_login import current_user
from flask_cors import CORS


def create_tcas(conf=None):
    """Initializes the TCAS application.

    Parameters
    ----------
    conf : dict or None

    Returns
    -------
    flask.Flask

    """
    from tcas.abstract import mod_abstract
    from tcas.admin import mod_admin
    from tcas.analysis import mod_analysis
    from tcas.auth import mod_auth
    from tcas.admin.model.page import Page
    from tcas.admin.model.pageview import Pageview
    from tcas.admin.model.upload import Upload
    from tcas.auth.model.user import User
    from tcas.abstract.model.case import Case
    from tcas.abstract.model.goal import Goal, FinancialGoal, MedicalGoal, SocialSupportGoal
    from tcas.abstract.model.goal_step import GoalStep
    from tcas.abstract.model.goal_step_type import GoalStepType
    from tcas.db import database_session, initialize_model
    from tcas.auth.helper import login_manager
    from tcas.config import APP_DIR

    application = Flask(__name__)
    CORS(application)
    application.config.from_envvar('TCAS_SETTINGS')
    initialize_model()
    application.register_blueprint(mod_abstract)
    application.register_blueprint(mod_admin)
    application.register_blueprint(mod_analysis)
    application.register_blueprint(mod_auth)

    login_manager.init_app(application)

    application.add_url_rule('/', 'index', lambda: jsonify(sorted([str(r) for r in application.url_map.iter_rules()])))

    @application.teardown_appcontext
    def shutdown_session(e):
        """Terminates session.

        Parameters
        ----------
        e : Exception

        Returns
        -------
        None

        """
        database_session.remove()

    @application.before_request
    def before_request():
        """Provides access to the current logged-in User to the application's global context.

        Returns
        -------
        None

        """
        g.user = current_user

    @application.errorhandler(400)
    @application.errorhandler(401)
    @application.errorhandler(404)
    @application.errorhandler(405)
    @application.errorhandler(500)
    def handle_bad_request(error):
        """Handles bad requests for given HTTP status codes.

        Parameters
        ----------
        error : werkzeug.exceptions.HTTPException

        Returns
        -------
        flask.wrappers.Response

        """
        return make_response(jsonify({error.name: error.description}), error.code)

    return application
