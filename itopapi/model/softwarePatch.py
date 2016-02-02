# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiSoftwarePatch is an abstraction of SoftwarePatch representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasSoftware import HasSoftware

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiSoftwarePatch(ItopapiPrototype, HasSoftware):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'SoftwarePatch',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'description', 'size'],
        'foreign_keys': [
            HasSoftware.foreign_key,
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiSoftwarePatch, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiSoftwarePatch, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiSoftwarePatch)

    """
    ItopapiSoftwarePatch is an object that represents an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiSoftwarePatch, self).__init__(data)

        self.description = None
        # Lists
        self.documents_list = {}
        self.softwareinstances_list = {}
