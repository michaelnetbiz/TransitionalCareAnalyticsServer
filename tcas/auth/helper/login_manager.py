# -*- coding: utf-8 -*-
from flask_login import LoginManager
from tcas.auth.model.user import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(_id):
    """Loads a user given an identifier.
    Parameters
    ----------
    _id

    Returns
    -------
    tcas.auth.model.user.User

    """
    user = User.query.filter_by(id=_id).first()
    if not user:
        return
    else:
        return user


# @login_manager.request_loader
# def load_user(request):
#     """ Loads a User given a Flask request
#     Parameters
#     ----------
#     request : flask.globals.request
#
#     Returns
#     -------
#     tcas.auth.model.user.User
#     """
#     print(request)
#     _id = request.args.get('_id')
#     token = request.args.get('token')
#     print(_id, token)
#     if not _id or not token:
#         return
#     user = User.query.filter_by(id=_id).first()
#     if not user:
#         return
#     else:
#         return user
