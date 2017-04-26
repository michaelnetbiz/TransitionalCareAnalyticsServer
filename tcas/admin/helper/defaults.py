# -*- coding: utf-8 -*-
from datetime import date

from tcas.config import VSSP_START_DATE

default_date_ranges = [{
    'startDate': VSSP_START_DATE,
    'endDate': str(date.today()),
}]

default_dimensions = [
    'ga:date',
    # 'ga:deviceCategory'
    'ga:dimension1',
    # 'ga:nthMinute',
    # 'ga:pagePath'
]

default_metrics = [
    # 'ga:bounceRate',
    # 'ga:avgSessionDuration',
    'ga:sessions',
    # 'ga:pageviews',
    # 'ga:uniquePageviews',
    # 'ga:timeOnPage',
    # 'ga:avgTimeOnPage',
    # 'ga:exitRate',
    # 'ga:pageviewsPerSession'
]
