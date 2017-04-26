# -*- coding: utf-8 -*-
def id_validator(_id, session, model):
    """

    Parameters
    ----------
    _id
    session
    model

    Returns
    -------

    """
    if len(session.query(model).filter_by(id=_id).all()) == 1:
        return True
    else:
        return False
