# -*- coding: utf8 -*-fr

"""
ItopapiPerson is a abstraction of a Person representation on iTop
Note : Person has no finalclass and name. It complicates things...
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPerson(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Person',
        # Define which fields to save when creating or updating from the python API
        'save': ['contact_id', 'contact_name'],
        'foreign_keys': [],
        'list_types': {},
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPerson, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPerson, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Person """
        return ItopapiPrototype.find_all(ItopapiPerson)

    """
    ItopapiPerson is an object that represents a Person from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPerson, self).__init__(data)
        self.contact_id = None
        self.contact_name = None
