def upload_extension_validator(filename):
    """Validates upload file extension.

    Parameters
    ----------
    filename : str
        Filename to test.

    Returns
    -------
    bool
        Return value indicates whether the input possesses one of the specified extensions.

    Usage example:

    >>> print(upload_extension_validator('lol.lol'))
    False

    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'zip', 'csv'}
