# -*- coding: utf8 -*-fr

"""
ItopapiContactType is an abstraction of ContactType representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.typology import ItopapiTypology

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiContactType(ItopapiTypology):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'ContactType',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ContactType with the given key or criteria """
        return ItopapiPrototype.find(ItopapiContactType, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiContactType, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of ContactType """
        return ItopapiPrototype.find_all(ItopapiContactType)

    """
    ItopapiContactType is an object that represents an ContactType from iTop
    """
    def __init__(self, data=None):
        super(ItopapiContactType, self).__init__(data)


# Register as a subclass of Typology
ItopapiTypology.register(ItopapiContactType)
