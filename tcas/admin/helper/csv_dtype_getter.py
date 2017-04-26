# -*- coding: utf-8 -*-
from pandas import read_csv


def csv_dtype_getter(src):
    """

    Parameters
    ----------
    src

    Returns
    -------

    """
    return read_csv(src).dtypes
