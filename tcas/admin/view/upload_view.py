from os import listdir, path
from werkzeug.utils import secure_filename

from flask import abort, jsonify, make_response, request
from flask.views import MethodView
from flask_login import current_user

from tcas.config import UPLOAD_DIR
from tcas.db import database_session as session
from tcas.helper.blueprint_router_mixin import BlueprintRouterMixin
from tcas.helper.id_validator import id_validator
from tcas.admin.model import Upload


class UploadView(BlueprintRouterMixin, MethodView):
    def get(self, _id):
        """

        :param _id: 
        :return: 
        """
        if not _id:
            return jsonify([user.serialize() for user in Upload.query.all()])
        elif Upload.query.filter_by(id=_id).all():
            return jsonify(Upload.query.filter_by(id=_id).first().serialize())
        else:
            return abort(404)

    def post(self):
        """

        :return: 
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
        """

        :param _id: 
        :return: 
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
