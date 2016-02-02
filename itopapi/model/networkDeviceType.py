# -*- coding: utf8 -*-fr

"""
ItopapiNetworkDeviceType is an abstraction of NetworkDeviceType representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.typology import ItopapiTypology

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiNetworkDeviceType(ItopapiTypology):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'NetworkDeviceType',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of NetworkDeviceType with the given key or criteria """
        return ItopapiPrototype.find(ItopapiNetworkDeviceType, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiNetworkDeviceType, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of NetworkDeviceType """
        return ItopapiPrototype.find_all(ItopapiNetworkDeviceType)

    """
    ItopapiNetworkDeviceType is an object that represents an NetworkDeviceType from iTop
    """
    def __init__(self, data=None):
        super(ItopapiNetworkDeviceType, self).__init__(data)

        # list of NetworkDevice(s) using this type.
        self.networkdevicesdevices = {}


# Register as a subclass of Typology
ItopapiTypology.register(ItopapiNetworkDeviceType)
