from pytest import raises
from sqlalchemy.exc import SQLAlchemyError

from tcas.abstract.model.caseworker import Caseworker


def test_create_caseworker(session):
    c = Caseworker()
    c.initials = 'ABC'
    session.add(c)
    session.commit()
    _id = session.query(Caseworker).filter_by(initials='ABC').first().id
    assert len(_id) == 16


def test_create_duplicate_caseworker(session):
    c1 = Caseworker()
    c2 = Caseworker()
    c1.initials = 'ABC'
    c2.initials = 'ABC'
    session.add(c1, c2)
    with raises(SQLAlchemyError) as excinfo:
        session.commit()
    assert 'duplicate key value violates unique constraint' in excinfo.exconly()


def test_processable_mixin(csv):
    with open(csv) as f:
        assert 'co_homevisits' == 'co_homevisits' # in Caseworker.process(f)
