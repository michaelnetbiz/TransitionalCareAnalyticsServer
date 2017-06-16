# -*- coding: utf-8 -*-
from psycopg2 import IntegrityError
from sqlalchemy.exc import IntegrityError
from flask import abort, jsonify, make_response, request
from flask.views import MethodView
from flask_login import login_required
from tcas.db import database_session as session
from tcas.auth.model.user import User
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.helper.endpoint_getter import endpoint_getter
from tcas.helper.id_validator import id_validator
from tcas.helper.url_getter import url_getter


class UserView(BlueprintRouterMixin, MethodView):
    """Provides interfaces for retrieving and acting upon User entities via HTTP requests.
    """

    @login_required
    def get(self, _id):
        """Returns metadata for either a single specified user, or all users.

        Parameters
        ----------
        _id

        Returns
        -------

        """
        if not _id:
            return jsonify([user.serialize() for user in User.query.all()])
        user = User.query.filter_by(id=_id).first()
        if not user:
            return abort(404)
        return jsonify(user.serialize())

    def post(self):
        """Creates a User.

        Returns
        -------

        """
        data = request.get_json()
        if not User.validate_post_data(data):
            return abort(400)
        s = session()
        email = data.get('email')
        pw = data.get('password')
        u = User(
            email=email,
            password=pw
        )
        s.add(u)
        try:
            s.commit()
        except IntegrityError:
            return abort(500)
        return make_response(jsonify({'email': email}), 201)

    # @login_required
    # def put(self, _id):
    #     data = request.get_json()
    #     if not User.validate_put_data(data):
    #         return abort(400)
    #     s = session()
    #     if not validate_id(_id, s, User):
    #         return abort(404)
    #     user = s.query(User).filter_by(id=_id).first()
    #     k = data.get('key')
    #     nv = data.get('new_value')
    #     pw = data.get('password')
    #     if not user.authenticate(pw):
    #         return abort(401)
    #     s.execute(update(User.__table__, values={User.__table__.c[k]: nv}))
    #     s.commit()
    #     return make_response(jsonify(User.query.order_by(User.date_updated.desc()).first().serialize()), 202)

    # @login_required
    def delete(self, _id):
        """

        Parameters
        ----------
        _id

        Returns
        -------

        """
        data = request.get_json()
        if not User.validate_delete_data(data):
            return abort(400)
        s = session()
        if not id_validator(_id, s, User):
            return abort(404)
        user = s.query(User).filter_by(id=_id).first()
        pw = data.get('password')
        if not user.authenticate(pw):
            return abort(401)
        s.delete(user)
        s.commit()
        return make_response(jsonify('Resource deleted successfully.'), 202)


user_endpoint = endpoint_getter(UserView)
user_converter = UserView.converter
user_key = UserView.key
user_url = url_getter(UserView)

user_view_func = UserView.as_view(user_endpoint)
