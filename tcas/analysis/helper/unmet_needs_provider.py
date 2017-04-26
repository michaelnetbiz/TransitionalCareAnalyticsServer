# -*- coding: utf-8 -*-
from pandas import read_csv

from tcas.config import MASTER_CSV


def unmet_needs_provider():
    """Provide unmet needs data.

    Returns
    -------

    """
    columns = [
        'ba_safehousing',
        'ba_needs',
        'ba_support',
        'ba_assistins',
        'ba_expensedif',
        'ba_assistentitle',
        'pa_appoint',
        'pa_medtake',
        'pa_unmetneeds',
        'pa_debilitate',
        'pa_needmental'
    ]
    return read_csv(MASTER_CSV, encoding='iso8859-2', na_values=['nan', ''])[columns]
