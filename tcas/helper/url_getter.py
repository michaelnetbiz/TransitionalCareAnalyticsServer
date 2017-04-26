# -*- coding: utf-8 -*-
from inflection import underscore


def url_getter(cls):
    """

    Parameters
    ----------
    cls

    Returns
    -------

    """
    return '/' + underscore(cls.__name__[:-4]).replace('_', '-') + '/'


