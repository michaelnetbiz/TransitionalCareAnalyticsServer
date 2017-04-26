from datetime import datetime
from werkzeug.utils import secure_filename


def report_name_generator(report_type):
    """
    Parameters
    report_requests : list

    Returns
    -------

    """
    return secure_filename(
        report_type.replace('_', '-')
        + '-generated-'
        + str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')
        + '.xlsx'
    )
