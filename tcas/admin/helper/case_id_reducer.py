# -*- coding: utf-8 -*-
from re import compile


def case_id_reducer(_id):
    """This function returns a reduced version of the patient/caregiver identifier.

    Parameters
    ----------
    _id : str :  The identifier to reduce.    

    Returns
    -------
    str
    
    Examples
    --------

    >>> print(case_id_reducer('a_p_005'))
    AP_005
    >>> print(case_id_reducer('PA-C_test'))
    PAC_TEST 
    """
    patterns = [compile(p) for p in ['test', 'TEST']]
    val = _id.replace('_', '').replace('-', '').upper()
    for p in patterns:
        if p.search(val):
            if len(val) - len(p.pattern) == 0:
                return val.lower()
            else:
                return val[:len(val) - len(p.pattern)].upper() + '_' + val[-len(p.pattern):]
    if val.isalpha():
        return val.lower()
    if val.isnumeric():
        return val.strip()
    if val[:3].isalpha():
        return val[:3] + '_' + val[3:]
    if val[:2].isalpha():
        return val[:2] + '_' + val[2:]
    else:
        return _id
