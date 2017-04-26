# -*- coding: utf-8 -*-
from json import loads

from flask import abort, request, make_response, jsonify
from flask.views import MethodView
from flask_login import login_user, logout_user
from itsdangerous import Serializer, SignatureExpired, BadSignature

from tcas.config import SECRET_KEY
from tcas.auth.model import User


class AuthView(MethodView):
    def post(self):
        """

        :return: 
        """
        data = request.get_json()
        token = data.get('token')
        mode = data.get('mode')
        if not token or not mode:
            return abort(400)
        s = Serializer(SECRET_KEY)
        try:
            _id = s.loads(loads(token).get('token')).get('id')
        except SignatureExpired:
            return make_response(jsonify('Token expired.'), 401)
        except BadSignature:
            return make_response(jsonify('Token invalid.'), 402)
        user = User.query.filter_by(id=_id).first()
        if not user:
            return abort(400)
        if mode == 'start':
            login_user(user)
            return make_response(jsonify('Authenticated successfully. Session started.'), 200)
        elif mode == 'finish':
            logout_user()
            return make_response(jsonify('Session ended successfully.'), 200)
        else:
            return abort(400)
