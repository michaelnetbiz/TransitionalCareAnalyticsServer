def upload_extension_validator(filename):
    """This function returns a uri.

        Args:
           filename (str):  The filename for which to test the extension.

        Returns:
           bool.  The return code::

              True -- The filename possesses one of the specified file extensions.
              False -- The filename does not possess one of the specified file extensions.

        Usage example:

        >>> print(upload_extension_validator('lol.lol'))
        False
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'zip', 'csv'}
