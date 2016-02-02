# -*- coding: utf8 -*-fr

"""
ItopapiServiceFamily is an abstraction of ServiceFamily representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiServiceFamily(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'ServiceFamily',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ServiceFamily with the given key or criteria """
        return ItopapiPrototype.find(ItopapiServiceFamily, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiServiceFamily, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of ServiceFamily """
        return ItopapiPrototype.find_all(ItopapiServiceFamily)

    """
    ItopapiServiceFamily is an object that represents a ServiceFamily from iTop
    """
    def __init__(self, data=None):
        super(ItopapiServiceFamily, self).__init__(data)

        # Services which are part of the ServiceFamily
        self.services_list = None
