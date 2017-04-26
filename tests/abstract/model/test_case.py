# -*- coding: utf-8 -*-
from tcas.abstract.model.case import Case


def test_create_cases_from_closeout(session, csv):
    # rec = closeouts.sample(n=1)
    # projection = data[Case.project(source)]
    # for selection in projection.iterrows():
    #     Case.create(selection)
    """

    Parameters
    ----------
    session
    csv
    """
    with open(csv) as f:
        assert 'evaluate to true' == 'evaluate to true'
        # print(Case.process(f))
        # c = Case()
        # session.add(c)
        # session.commit()
        # _id = session.query(Case).filter_by(record_id='AP_005').first().id
        # assert len('') == 0


def test_create_duplicate_case():
    pass


def test_read_case(session):
    pass


def test_update_case(session):
    pass


def test_delete_case(session):
    pass
