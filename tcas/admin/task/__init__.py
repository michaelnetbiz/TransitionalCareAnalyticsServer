# -*- coding: utf-8 -*-
"""
.. module:: tcas.admin.task
   :platform: idk
   :synopsis: Module for administering computationally intensive and periodic tasks.

.. moduleauthor:: Michael E. Nelson <michael.nelson@fulbrightmail.org>

"""
from datetime import date
from tcas.admin.model.report import Report
from tcas.admin.model.report_request import ReportRequest
from tcas.admin.service import report_service as service
from tcas.task_manager import task_manager


@task_manager.task()
def abstract_variable(variable_abstractee):
    """

    Parameters
    ----------
    variable_abstractee

    Returns
    -------
    str

    """
    return variable_abstractee


# TODO: implement parser for .smcl (see cli options)

divider_head = '-------------------------------------------------------------------------------\n'
divider_tail = '\n\n-------------------------------------------------------------------------------\n'


class Variable(object):
    name = None
    description = None
    data_type = None
    label = None
    range = None
    n_unique_values = None
    units = None
    missing = None
    examples = None
    txt = None
    tabulation = None
    warning = None
    percentiles = None
    std_dev = None
    mean = None

    def __init__(self, txt):
        self.txt = txt
        self.process()

    def get_name(self):
        line_2 = self.txt.lstrip(divider_head)
        self.name = line_2[:line_2.find(' ')]

    def get_description(self):
        line_2 = self.txt.lstrip(divider_head)
        self.description = line_2.lstrip(self.name).lstrip().split('\n')[0]

    def get_data_type(self):
        line_5 = self.txt[self.txt.find('\n', 79 * 3, -1):]
        self.data_type = line_5.lstrip('\n\n                  type:  ').lstrip().split('\n')[0]

    def process(self):
        self.get_name()
        self.get_description()
        self.get_data_type()


def extract_variables(fileobj):
    return [Variable(line) for line in fileobj.read().split(divider_tail)]


def resolve_codebook_data_type(cdt):
    if cdt == 'numeric (long)':
        return float
    elif cdt == 'numeric (int)':
        return int
    elif cdt == 'numeric (byte)':
        return bytes
    elif cdt.startswith('string'):
        return str
    elif cdt == 'numeric daily date (float)':
        return date


def get_n_line(n, txt):
    n = 79 * (n - 1)
    return txt[n:n - len(txt)]


# with open('data/export/codebook_no_comments.txt') as tf:
#     variables = extract_variables(tf)
#     tf.close()


@task_manager.task()
def run_google_analytics_report():
    """Run reporting task.

    Returns
    -------

    """
    pageviews_per_user = ReportRequest('pageviews_per_user')
    pageviews_per_user_with_path = ReportRequest('pageviews_per_user_with_path')
    pageviews_per_user_with_path_by_date = ReportRequest('pageviews_per_user_with_path_by_date')
    sessions_per_user = ReportRequest('sessions_per_user')
    sessions_per_user_by_date = ReportRequest('sessions_per_user_by_date')
    unique_pageviews_per_user = ReportRequest('unique_pageviews_per_user')
    unique_pageviews_per_user_with_path = ReportRequest('unique_pageviews_per_user_with_path')
    unique_pageviews_per_user_with_path_by_date = ReportRequest('unique_pageviews_per_user_with_path_by_date')

    reports = [
        # pageviews_per_user,
        # pageviews_per_user_with_path,
        pageviews_per_user_with_path_by_date,
        # sessions_per_user,
        sessions_per_user_by_date,
        # unique_pageviews_per_user,
        # unique_pageviews_per_user_with_path,
        unique_pageviews_per_user_with_path_by_date
    ]

    for report in reports:
        report = Report(service, report)
        report.parse()
        report.export()
