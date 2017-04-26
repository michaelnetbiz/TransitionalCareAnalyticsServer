# -*- coding: utf-8 -*-
from pandas import read_csv
from typing import Iterable


def csv_data_type_getter(fp: str) -> Iterable:
    """

    Parameters
    ----------
    fp

    Returns
    -------

    """
    if isinstance(fp, str) and fp.endswith('csv'):
        with open(fp) as cf:
            items = read_csv(cf, error_bad_lines=False, warn_bad_lines=False).dtypes.to_dict().items()
            cf.close()
            return items
