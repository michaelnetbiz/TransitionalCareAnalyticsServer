# -*- coding: utf-8 -*-
from json import dumps, loads
from flask import abort, g, request, make_response, jsonify
from flask.views import MethodView
from flask_login import login_user, logout_user, login_required
from itsdangerous import Serializer, SignatureExpired, BadSignature
from tcas.config import SECRET_KEY
from tcas.helper.endpoint_getter import endpoint_getter
from tcas.auth.model.user import User


class AuthView(MethodView):
    """Provides interfaces for retrieving and acting upon Authenticated User entities via HTTP requests.
    """

    @login_required
    def get(self):
        token = g.user.generate_token()
        return jsonify({'token': token.decode('ascii')})

    def post(self):
        """Authenticates specified User using the provided combination of email and password.
        Returns
        -------
        """
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return abort(400)
        are_credentials_verified = User.verify_credentials(email, password)
        if not are_credentials_verified:
            return abort(401)
        else:
            user = User.query.filter_by(email=email).first()
            login_user(user)
            return make_response(jsonify('Authenticated successfully. Session started.'), 200)

            # token = data.get('token')
            # mode = data.get('mode')
            # if not token or not mode:
            #     return abort(400)
            # s = Serializer(SECRET_KEY)
            # try:
            #     _id = s.loads(token).get('id')
            # except SignatureExpired:
            #     return make_response(jsonify('Token expired.'), 401)
            # except BadSignature:
            #     return make_response(jsonify('Token invalid.'), 402)
            # user = User.query.filter_by(id=_id).first()
            # if not user:
            #     return abort(400)
            # if mode == 'start':
            #     login_user(user)
            #     return make_response(jsonify('Authenticated successfully. Session started.'), 200)
            # elif mode == 'finish':
            #     logout_user()
            #     return make_response(jsonify('Session ended successfully.'), 200)
            # else:
            #     return abort(400)


auth_endpoint = endpoint_getter(AuthView)
auth_url = '/'
auth_view_func = AuthView.as_view(auth_endpoint)
