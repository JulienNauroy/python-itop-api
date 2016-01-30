# -*- coding: utf8 -*-fr

"""
ItopapiLocation is an abstraction of a Location representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiLocation(ItopapiPrototype, HasOrganization):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Location',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'address', 'postal_code', 'city', 'country'],
        'foreign_keys': [
            HasOrganization.foreign_key,
        ],
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of OSFamily with the given key or criteria """
        return ItopapiPrototype.find(ItopapiLocation, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiLocation, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiLocation)

    """
    ItopapiLocation is an object that represents an OS Family from iTop
    """
    def __init__(self, data=None):
        super(ItopapiLocation, self).__init__(data)
        # Location's status. Values within [inactive, active]
        self.status = None
        # Location's street address. Generally multiline
        self.address = None
        self.postal_code = None
        self.city = None
        self.country = None
        # Lists
        self.person_list = {}
        self.physicaldevice_list = {}
