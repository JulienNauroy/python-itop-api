# -*- coding: utf8 -*-fr

"""
ItopapiPowerConnection is an abstraction of Connectable CI representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.physicalDevice import ItopapiPhysicalDevice

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPowerConnection(ItopapiPhysicalDevice):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'PowerConnection',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Connectable CI with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPowerConnection, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPowerConnection, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Connectable CI """
        return ItopapiPrototype.find_all(ItopapiPowerConnection)

    """
    ItopapiPowerConnection is an object that represents a Connectable CI from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPowerConnection, self).__init__(data)


# Register as a subclass of PhysicalDevice
ItopapiPhysicalDevice.register(ItopapiPowerConnection)