from flask import jsonify
from flask.views import MethodView
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.admin.model import Page


class PageView(BlueprintRouterMixin, MethodView):
    """Provides interfaces for retrieving and acting upon Page entities via HTTP requests.
    """
    def get(self, _id):
        """

        Parameters
        ----------
        _id

        Returns
        -------

        """
        if _id is None:
            return jsonify([user.serialize() for user in Page.query.all()])
        else:
            return jsonify(Page.query.filter_by(id=_id).all())
