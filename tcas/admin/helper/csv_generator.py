from csv import DictWriter
from os import fdopen
from random import randint
from tempfile import mkstemp

from tcas.helper import csv_fieldname_extractor, csv_dtype_getter


def csv_generator(src, case_ids):
    """This function generates a csv for tests to use as a fixture.
    Parameters
    ----------
    src : str 
    case_ids : list
        
    >>> csv_generator('master.csv')
    <csv.DictReader object at 0x1121d1358>
    """
    h, fp = mkstemp(suffix='.csv')
    fieldnames = csv_fieldname_extractor(src)
    # dtypes = get_dtypes(src)
    with fdopen(h, mode='w') as csvfile:
        w = DictWriter(csvfile, fieldnames=fieldnames)
        w.writeheader()
        for _id in case_ids:
            row = {f: randint(100, 999) for f in fieldnames}
            row['id'] = _id
            w.writerow(row)
    return fp
