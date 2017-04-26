# -*- coding: utf-8 -*-
from os import path

from pandas import DataFrame

from tcas.config import DOWNLOAD_DIR
from tcas.admin.helper.case_id_reducer import case_id_reducer
from tcas.admin.helper.report_name_generator import report_name_generator


class Report(object):
    """Represent a Google Analytics Report.

    """

    @staticmethod
    def format_ga_date(ga_date):
        """

        Parameters
        ----------
        ga_date

        Returns
        -------
        str
        """
        return ga_date[:4] + '-' + ga_date[4:6] + '-' + ga_date[6:]

    """Represent a Google Analytics Report.
    """

    def __init__(self, service, report_request):
        """Instantiate a Report.

        Parameters
        ----------
        report_request : :obj:`ReportRequest`
            Description of `report_request`. 
            
        """
        self.n = 1
        self.response = service(body={'reportRequests': report_request.serialize()}).execute()
        self.filename = report_name_generator(report_request.type)
        self.path = path.join(DOWNLOAD_DIR, self.filename)

    def get_dimensions(self):
        """Get an instance's dimensions.

        """
        rv = []
        res = self.response
        for i in range(self.n):
            metadata = res['reports'][i]['columnHeader']
            dimensions = [dimension for dimension in metadata['dimensions']]
            rv.append(dimensions)
        return rv

    def get_metrics(self):
        """Get an instance's metrics.

        """
        rv = []
        res = self.response
        for i in range(self.n):
            metadata = res['reports'][i]['columnHeader']
            metrics = [metric['name'] for metric in metadata['metricHeader']['metricHeaderEntries']]
            rv.append(metrics)
        return rv

    def parse(self):
        """

        Returns
        -------

        """
        rv = {}
        res = self.response
        for i in range(self.n):
            report = []
            metadata = res['reports'][i]['columnHeader']
            data = res['reports'][i]['data']
            dimensions = [dimension for dimension in metadata['dimensions']]
            metrics = [metric['name'] for metric in metadata['metricHeader']['metricHeaderEntries']]
            if not data['rows']:
                raise Exception
            for j in data['rows']:
                row = {}
                for d in dimensions:
                    row[d] = j['dimensions'][dimensions.index(d)]
                for m in metrics:
                    row[m] = j['metrics'][0]['values'][metrics.index(m)]
                report.append(row)
            rv[i] = report
        return rv

    def export(self):
        """

        Returns
        -------

        """
        data = self.parse()
        dfs = {k: DataFrame(v) for k, v in data.items()}
        for df in dfs.items():
            i, df = df
            df['ga:dimension1'] = df['ga:dimension1'].apply(case_id_reducer)
            if 'ga:date' in df.columns:
                df['ga:date'] = df['ga:date'].apply(Report.format_ga_date)
            df = df.groupby(
                by=self.get_dimensions()[self.n - 1]
            ).sum()
            df[self.get_metrics()[self.n - 1]] = df[self.get_metrics()[self.n - 1]].astype(int)
            df.to_excel(self.path, sheet_name='Sheet' + str(i + 1))
        return self.filename
