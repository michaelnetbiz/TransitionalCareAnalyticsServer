# -*- coding: utf-8 -*-
from csv import DictReader


def csv_fieldname_extractor(src):
    """This function extracts fieldnames from the specified .csv file.

    Parameters
    ----------
    src : str
        The path of the file to extract from.

    Returns
    -------
    list
    
    Examples
    --------

    >>> print(csv_fieldname_extractor('master.csv'))
    ['id', 'date', 'etc']
    """
    with open(src) as csvfile:
        master = DictReader(csvfile)
        fieldnames = master.fieldnames
        csvfile.close()
        return fieldnames
