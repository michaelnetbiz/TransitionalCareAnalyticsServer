# -*- coding: utf-8 -*-
from inflection import underscore

token_level_view_args = {'_id': None}
type_level_view_args = {'_name': None}


class BlueprintRouterMixin(object):
    """Provides methods for generating endpoints and URLs based on the class that uses the mixin.

    Attributes
    ----------
    converter : str
    key : str

    """

    @staticmethod
    def get_endpoint(cls):
        """Provides endpoint for a given class.

        Parameters
        ----------
        cls

        Returns
        -------
        str

        """
        return underscore(cls.__name__)

    @staticmethod
    def get_url(cls):
        """Provides url for a given class.

        Parameters
        ----------
        cls

        Returns
        -------
        str

        """
        return '/' + underscore(cls.__name__[:-4]).replace('_', '-') + '/'

    converter = 'string'
    key = '_id'
