# -*- coding: utf-8 -*-
from inflection import underscore


def endpoint_getter(cls):
    """

    Parameters
    ----------
    cls

    Returns
    -------

    """
    return underscore(cls.__name__)
