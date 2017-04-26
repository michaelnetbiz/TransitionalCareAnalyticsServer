# -*- coding: utf-8 -*-
import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

# application path variables
APP_DIR = os.path.abspath(os.path.dirname(__file__))
DOWNLOAD_DIR = os.path.join(APP_DIR, os.getenv('DOWNLOAD_DIR'))
PROJECT_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))
TMP_DIR = os.path.join(APP_DIR, os.getenv('TMP_DIR'))
UPLOAD_DIR = os.path.join(APP_DIR, os.getenv('UPLOAD_DIR'))

# project path variables
DATA_DIR = os.path.join(PROJECT_DIR, os.getenv('DATA_DIR'))
EXPORT_DIR = os.path.join(DATA_DIR, os.getenv('EXPORT_DIR'))
MASTER_CSV = os.path.join(EXPORT_DIR, os.getenv('MASTER_CSV'))
MIGRATION_DIR = os.path.join(PROJECT_DIR, os.getenv('MIGRATION_DIR'))
SITEDUMP_DIR = os.path.join(DATA_DIR, os.getenv('SITEDUMP_DIR'))

# Flask and Flask extension variables
CSRF_ENABLED = os.getenv('CSRF_ENABLED')
CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')
DEBUG = os.getenv('DEBUG')
MAX_CONTENT_LENGTH = 8 * 1024 * 1024
SECRET = os.getenv('SECRET')
SECRET_KEY = os.getenv('SECRET_KEY')
SESSION_TYPE = 'filesystem'

# db variables
DATABASE_URI = os.getenv('DATABASE_URI')

# auth module variables
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
TESTING_USER_EMAIL = os.getenv('TESTING_USER_EMAIL')
TESTING_USER_PASSWORD = os.getenv('TESTING_USER_PASSWORD')

# lang module variables
CONTRACTIONS = os.path.join(DATA_DIR, os.getenv('CONTRACTIONS'))
ENGLISH_PICKLE = os.path.join(DATA_DIR, os.getenv('ENGLISH_PICKLE'))
GOAL_TOKENS = os.path.join(DATA_DIR, os.getenv('GOAL_TOKENS'))
GOALS_OUT = os.path.join(EXPORT_DIR, os.getenv('GOALS_OUT'))
NUMERALS = os.path.join(DATA_DIR, os.getenv('NUMERALS'))

# service module variables
GA_PROPERTY_ID = os.getenv('GA_PROPERTY_ID')
GA_SERVICE_ACCOUNT_CREDENTIALS = os.path.join(PROJECT_DIR, os.getenv('GA_SERVICE_ACCOUNT_CREDENTIALS'))
GA_SERVICE_ACCOUNT_SCOPE = os.getenv('GA_SERVICE_ACCOUNT_SCOPE')
GA_VIEW_ID = os.getenv('GA_VIEW_ID')
VSSP_START_DATE = os.getenv('VSSP_START_DATE')

# task module variables
TASK_BACKEND = os.getenv('TASK_BACKEND')
TASK_BROKER = os.getenv('TASK_BROKER')

# test fixture variables
CASE_IDS = os.getenv('CASE_IDS')
