# -*- coding: utf-8 -*-
from flask import abort, request
from flask.views import MethodView
from tcas.helper.endpoint_getter import endpoint_getter
from tcas.helper.url_getter import url_getter
from tcas.task_manager import task_manager
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.abstract.task import abstract_cases, abstract_goals
from tcas.admin.task import abstract_variable, run_google_analytics_report
from tcas.analysis.task import cluster_goals


class TaskView(BlueprintRouterMixin, MethodView):
    """Provides interfaces for retrieving and acting upon Task entities via HTTP requests.
    """
    def get(self, _id):
        """Provides metadata (namely, current status) for a given task.
        """
        task_name = request.args.get('task_name')
        if task_name:
            async_task = cluster_goals.AsyncResult(_id)
            return async_task.state
        else:
            return abort(400)


task_endpoint = endpoint_getter(TaskView)
task_url = url_getter(TaskView)
task_converter = TaskView.converter
task_key = TaskView.key

task_view_func = TaskView.as_view(task_endpoint)
