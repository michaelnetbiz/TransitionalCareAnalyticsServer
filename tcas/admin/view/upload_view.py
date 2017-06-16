# -*- coding: utf-8 -*-
from os import listdir, path
from werkzeug.utils import secure_filename
from flask import abort, jsonify, make_response, request
from flask.views import MethodView
from tcas.config import UPLOAD_DIR
from tcas.db import database_session as session
from tcas.helper.endpoint_getter import endpoint_getter
from tcas.helper.url_getter import url_getter
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.helper.id_validator import id_validator
from tcas.admin.model.upload import Upload


class UploadView(BlueprintRouterMixin, MethodView):
    def get(self, _id):
        """Reads a specified Upload resource or else returns all Upload resources.

        Parameters
        ----------
        _id

        Returns
        -------

        """
        if not _id:
            return jsonify([user.serialize() for user in Upload.query.all()])
        elif Upload.query.filter_by(id=_id).all():
            return jsonify(Upload.query.filter_by(id=_id).first().serialize())
        else:
            return abort(404)

    def post(self):
        """Creates an Upload resource.

        Returns
        -------

        """
        f = request.files['file']
        filename = secure_filename(path.split(f.filename)[1])
        upload_dir = UPLOAD_DIR
        if filename in listdir(upload_dir):
            return make_response(jsonify('Resource of that name filename already exists.'), 400)
        elif not filename.endswith('csv'):
            return make_response(jsonify('Resource must consist of comma-separated values.'), 400)
        else:
            s = session()
            p = path.join(upload_dir, filename)
            u = Upload(p)
            f.save(p)
            s.add(u)
            s.commit()
            return make_response(jsonify('Resource created successfully.'), 201)

    def delete(self, _id):
        """Detroys an Upload resource.

        Parameters
        ----------
        _id

        Returns
        -------

        """
        if Upload.validate_delete_data(request.get_json()):
            s = session()
            data = request.get_json()
        else:
            return abort(400)
        if id_validator(_id, s, Upload):
            upload = s.query(Upload).filter_by(id=_id).first()
        else:
            return abort(404)
        s.delete(upload)
        s.commit()
        return make_response(jsonify('Resource deleted successfully'), 202)


upload_endpoint = endpoint_getter(UploadView)
upload_url = url_getter(UploadView)
upload_converter = UploadView.converter
upload_key = UploadView.key

upload_view_func = UploadView.as_view(upload_endpoint)
