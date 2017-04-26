# -*- coding: utf-8 -*-
from flask import jsonify, redirect, url_for
from flask.views import MethodView
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.abstract.model.case import Case
from tcas.abstract.task import abstract_cases
from tcas.helper.endpoint_getter import endpoint_getter
from tcas.helper.url_getter import url_getter


class CaseView(BlueprintRouterMixin, MethodView):
    def get(self, _id):
        """

        Parameters
        ----------
        _id

        Returns
        -------

        """
        if _id is None:
            return jsonify([user.serialize() for user in Case.query.all()])
        else:
            return jsonify(Case.query.filter_by(id=_id).all())

    def post(self):
        """Run goal abstraction task asynchronously.

        """
        task = abstract_cases.apply_async(args=['arg'])
        return url_for('abstract.case_view', task_id=task.id)


case_endpoint = endpoint_getter(CaseView)
case_url = url_getter(CaseView)
case_converter = CaseView.converter
case_key = CaseView.key
case_view_func = CaseView.as_view(case_endpoint)
