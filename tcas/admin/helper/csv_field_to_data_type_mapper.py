# -*- coding: utf-8 -*-
from tcas.helper import csv_unzipper


def csv_field_to_data_type_mapper(src, doc) -> map:
    """Determines data types given a .csv file.

    Parameters
    ----------
    src
    doc

    Returns
    -------

    """
    return ([
        {
            g[0]: map(
                lambda x: dict({
                    x[0]: x[1].name
                }),
                g[1].dtypes.to_dict().items()
            )
        }
        for g in csv_unzipper(src) if g[0] == doc
    ])
