# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiOSPatch is an abstraction of OSPatch representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOSVersion import HasOSVersion

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiOSPatch(ItopapiPrototype, HasOSVersion):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'OSPatch',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'description', 'size'],
        'foreign_keys': [
            HasOSVersion.foreign_key,
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiOSPatch, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiOSPatch, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiOSPatch)

    """
    ItopapiOSPatch is an object that represents an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiOSPatch, self).__init__(data)

        self.description = None
        # Lists
        self.documents_list = {}
        self.functionalcis_list = {}
