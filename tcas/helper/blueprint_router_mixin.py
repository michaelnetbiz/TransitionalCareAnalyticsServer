# -*- coding: utf-8 -*-
from inflection import underscore

token_level_view_args = {'_id': None}
type_level_view_args = {'_name': None}


class BlueprintRouterMixin(object):
    @staticmethod
    def get_endpoint(cls):
        """

        Parameters
        ----------
        cls

        Returns
        -------

        """
        return underscore(cls.__name__)

    @staticmethod
    def get_url(cls):
        """

        Parameters
        ----------
        cls

        Returns
        -------

        """
        return '/' + underscore(cls.__name__[:-4]).replace('_', '-') + '/'

    key = '_id'

    converter = 'string'
