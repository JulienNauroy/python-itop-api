# -*- coding: utf8 -*-fr

"""
ItopapiPhysicalDevice is an abstraction of Physical Device representation on iTop
It serves as a base class for Racks Servers and much more.
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.functionalCI import ItopapiFunctionalCI

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPhysicalDevice(ItopapiFunctionalCI):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'PhysicalDevice',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Physical Device with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPhysicalDevice, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPhysicalDevice, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Physical Device """
        return ItopapiPrototype.find_all(ItopapiPhysicalDevice)

    """
    ItopapiPhysicalDevice is an object that represents a Physical Device from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPhysicalDevice, self).__init__(data)

# Register as a subclass of FunctionalCI
ItopapiFunctionalCI.register(ItopapiPhysicalDevice)
