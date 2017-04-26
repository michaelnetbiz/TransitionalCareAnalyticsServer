# -*- coding: utf-8 -*-
from json import dumps, loads

from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from tcas import create_tcas
from tcas.db import initialize_model, reset_model
from tcas.config import CASE_IDS, DATABASE_URI, MASTER_CSV, TESTING_USER_EMAIL, TESTING_USER_PASSWORD

from tcas.helper import csv_generator


@fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application.

    Parameters
    ----------
    request

    Returns
    -------

    """
    application = create_tcas()

    ctx = application.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    with application.test_client() as client:
        res1 = client.post(
            path='/auth/user/',
            headers=[('Content-Type', 'application/json')],
            data=dumps({
                'email': TESTING_USER_EMAIL,
                'password': TESTING_USER_PASSWORD
            })
        )
        token = res1.get_data()
        res2 = client.post(
            path='/auth/',
            headers=[('Content-Type', 'application/json')],
            data=dumps({
                'token': token.decode(),
                'mode': 'start'
            })
        )

    request.addfinalizer(teardown)
    return application


@fixture(scope='session')
def db(request):
    """Session-wide test database.

    Parameters
    ----------
    request

    Returns
    -------

    """
    engine = create_engine(DATABASE_URI, convert_unicode=True)

    def teardown():
        reset_model(engine)

    initialize_model(engine)
    request.addfinalizer(teardown)
    return engine


@fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test.

    Parameters
    ----------
    db
    request

    Returns
    -------

    """
    database_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db))

    def teardown():
        """

        """
        database_session.remove()

    request.addfinalizer(teardown)
    return database_session


@fixture(scope='function')
def csv():
    """

    Returns
    -------

    """
    return csv_generator(MASTER_CSV, CASE_IDS)
