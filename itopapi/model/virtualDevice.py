# -*- coding: utf8 -*-fr

"""
ItopapiVirtualDevice is an abstraction of VirtualDevice representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.functionalCI import ItopapiFunctionalCI

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiVirtualDevice(ItopapiFunctionalCI):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'VirtualDevice',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of VirtualDevice with the given key or criteria """
        return ItopapiPrototype.find(ItopapiVirtualDevice, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiVirtualDevice, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of VirtualDevice """
        return ItopapiPrototype.find_all(ItopapiVirtualDevice)

    """
    ItopapiVirtualDevice is an object that represents a VirtualDevice from iTop
    """
    def __init__(self, data=None):
        super(ItopapiVirtualDevice, self).__init__(data)


# Register as a subclass of FunctionalCI
ItopapiFunctionalCI.register(ItopapiVirtualDevice)
