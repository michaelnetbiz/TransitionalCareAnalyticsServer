# -*- coding: utf-8 -*-
from flask import abort, jsonify, make_response, url_for
from flask.views import MethodView
from tcas.analysis.task import cluster_goals
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.helper.endpoint_getter import endpoint_getter
from tcas.helper.url_getter import url_getter


class ClusteringView(BlueprintRouterMixin, MethodView):
    """Provides view of clustering analysis for a given entity.
    """

    def __init__(self, entity):
        self.entity = entity

    def get(self):
        """Run clustering task asynchronously
        Returns
        -------
        """
        if self.entity == 'goal':
            async_task = cluster_goals.apply_async()
            return make_response(jsonify({
                'uri': url_for('admin.task_view', _id=async_task.id, task_name=__name__)
            }), 200)
        else:
            return abort(400)


clustering_endpoint = endpoint_getter(ClusteringView)
clustering_url = url_getter(ClusteringView)
clustering_converter = ClusteringView.converter
clustering_key = ClusteringView.key

clustering_view_func = ClusteringView.as_view(clustering_endpoint, 'goal')
