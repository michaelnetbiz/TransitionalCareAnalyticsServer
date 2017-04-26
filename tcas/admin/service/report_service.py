# -*- coding: utf-8 -*-
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

from tcas.config import GA_SERVICE_ACCOUNT_CREDENTIALS, GA_SERVICE_ACCOUNT_SCOPE

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    GA_SERVICE_ACCOUNT_CREDENTIALS,
    scopes=[GA_SERVICE_ACCOUNT_SCOPE]
)

ga_service = build(
    'analytics',
    'v4',
    http=credentials.authorize(Http())
)

report_service = ga_service.reports().batchGet
