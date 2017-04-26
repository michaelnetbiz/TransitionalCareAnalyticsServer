from flask import jsonify
from flask.views import MethodView
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.admin.model import Pageview


# TODO: link pageviews to goals (met/unment) if pageview is of a relevant page
class PageviewView(BlueprintRouterMixin, MethodView):
    def get(self, _id):
        """

        Parameters
        ----------
        _id

        Returns
        -------

        """
        if _id is None:
            return jsonify([user.serialize() for user in Pageview.query.all()])
        else:
            return jsonify(Pageview.query.filter_by(id=_id).all())
