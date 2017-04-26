# -*- coding: utf-8 -*-
from flask import jsonify
from flask.views import MethodView
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.abstract.model.goal import Goal
from tcas.helper.endpoint_getter import endpoint_getter
from tcas.helper.url_getter import url_getter


class GoalView(BlueprintRouterMixin, MethodView):
    def get(self, _id):
        """

        :param _id: 
        :return: 
        """
        if _id is None:
            return jsonify([user.serialize() for user in Goal.query.all()])
        else:
            return jsonify(Goal.query.filter_by(id=_id).all())


goal_endpoint = endpoint_getter(GoalView)
goal_url = url_getter(GoalView)
goal_converter = GoalView.converter
goal_key = GoalView.key
goal_view_func = GoalView.as_view(goal_endpoint)