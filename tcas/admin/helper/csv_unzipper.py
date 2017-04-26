# -*- coding: utf-8 -*-
from zipfile import ZipFile as z

from pandas import read_csv


def csv_unzipper(path):
    """

    Parameters
    ----------
    path

    Returns
    -------

    """
    return [tuple([c, read_csv(z(path).open(c))]) for c in z(path).namelist() if not c.startswith('_')]
