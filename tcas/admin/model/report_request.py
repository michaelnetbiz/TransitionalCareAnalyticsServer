# -*- coding: utf-8 -*-
from tcas.config import GA_VIEW_ID
from tcas.admin.helper import default_date_ranges


class ReportRequest(object):
    """Represent a Google Analytics Report Request.

    """

    ALLOWED_REPORTS = {
        'sessions_per_user': {
            'dimensions': ['ga:dimension1'],
            'metrics': ['ga:sessions']
        },

        'sessions_per_user_by_date': {
            'dimensions': ['ga:dimension1', 'ga:date'],
            'metrics': ['ga:sessions']
        },

        'unique_pageviews_per_user': {
            'dimensions': ['ga:dimension1'],
            'metrics': ['ga:uniquePageviews']
        },

        'unique_pageviews_per_user_with_path': {
            'dimensions': ['ga:dimension1', 'ga:pagePath'],
            'metrics': ['ga:uniquePageviews']
        },

        'unique_pageviews_per_user_with_path_by_date': {
            'dimensions': ['ga:dimension1', 'ga:pagePath', 'ga:date'],
            'metrics': ['ga:uniquePageviews']
        },

        'pageviews_per_user': {
            'dimensions': ['ga:dimension1'],
            'metrics': ['ga:pageviews']
        },

        'pageviews_per_user_with_path': {
            'dimensions': ['ga:dimension1', 'ga:pagePath'],
            'metrics': ['ga:pageviews']
        },

        'pageviews_per_user_with_path_by_date': {
            'dimensions': ['ga:dimension1', 'ga:pagePath', 'ga:date'],
            'metrics': ['ga:pageviews']
        }
    }

    def __init__(self, report_type):
        """Instantiate a ReportRequest.

        Parameters
        ----------
        report_type : str

        """
        self.type = ReportRequest.validate(report_type)
        self.dimensions = ReportRequest.ALLOWED_REPORTS[self.type]['dimensions'],
        self.metrics = ReportRequest.ALLOWED_REPORTS[self.type]['metrics'],
        self.parameters = {
            'dateRanges': default_date_ranges,
            'dimensions': [{'name': d} for d in self.dimensions[0]],
            'metrics': [{'expression': m} for m in self.metrics[0]],
            'viewId': GA_VIEW_ID
        }

    def serialize(self):
        """

        Returns
        -------

        """
        return {key: value for (key, value) in self.parameters.items()}

    @staticmethod
    def validate(report_type):
        """Validate report-type constructor method argument

        Parameters
        ----------
        report_type

        Returns
        -------

        """
        if '-' in report_type:
            report_type = report_type.replace('-', '_')
        if report_type not in ReportRequest.ALLOWED_REPORTS.keys():
            return None
        else:
            return report_type
