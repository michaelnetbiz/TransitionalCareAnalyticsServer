# -*- coding: utf-8 -*-
from flask_login import LoginManager
from tcas.auth.model import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(_id):
    """

    :param _id: 
    :return: 
    """
    return User.query.filter_by(id=_id).first()
