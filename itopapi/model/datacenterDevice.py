# -*- coding: utf8 -*-fr

"""
ItopapiDatacenterDevice is an abstraction of Datacenter Device representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.connectableCI import ItopapiConnectableCI

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiDatacenterDevice(ItopapiConnectableCI):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'DatacenterDevice',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Datacenter Device with the given key or criteria """
        return ItopapiPrototype.find(ItopapiDatacenterDevice, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiDatacenterDevice, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Datacenter Device """
        return ItopapiPrototype.find_all(ItopapiDatacenterDevice)

    """
    ItopapiDatacenterDevice is an object that represents a Datacenter Device from iTop
    """
    def __init__(self, data=None):
        super(ItopapiDatacenterDevice, self).__init__(data)


# Register as a subclass of ConnectableCI
ItopapiConnectableCI.register(ItopapiDatacenterDevice)