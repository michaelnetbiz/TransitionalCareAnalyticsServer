# -*- coding: utf-8 -*-
def ga_date_formatter(series):
    """

    Parameters
    ----------
    series

    Returns
    -------

    """
    if series.name != 'ga:date':
        return series
    else:
        return series.apply(lambda x: str(x)[:4] + '-' + str(x)[4:6] + '-' + str(x)[6:])
