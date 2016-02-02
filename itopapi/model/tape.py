# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiTape is an abstraction of Tape representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasTapeLibrary import HasTapeLibrary

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiTape(ItopapiPrototype, HasTapeLibrary):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Tape',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'description', 'size'],
        'foreign_keys': [
            HasTapeLibrary.foreign_key,
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiTape, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiTape, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiTape)

    """
    ItopapiTape is an object that represents an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiTape, self).__init__(data)

        self.description = None
        self.size = None
