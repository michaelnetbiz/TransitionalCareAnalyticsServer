from flask import send_from_directory, abort
from flask.views import MethodView
from googleapiclient.errors import HttpError

from tcas.admin.model import Report, ReportRequest
from tcas.admin.service import report_service as service
from tcas.config import DOWNLOAD_DIR


class ReportView(MethodView):
    def get(self, _name):
        """

        Parameters
        ----------
        _name : str

        Returns
        -------

        """
        if not _name:
            report_request = ReportRequest('sessions-per-user-by-date')
        else:
            try:
                report_request = ReportRequest(_name)
            except KeyError:
                return abort(404)
        try:
            report = Report(service, report_request)
        except HttpError as e:
            return e, abort(400)
        report.parse()
        report_file = report.export()
        return send_from_directory(DOWNLOAD_DIR, report_file, as_attachment=True)
