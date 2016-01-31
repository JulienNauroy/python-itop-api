# -*- coding: utf8 -*-fr

"""
ItopapiSoftwareInstance is an abstraction of Software Instance representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.functionalCI import ItopapiFunctionalCI

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiSoftwareInstance(ItopapiFunctionalCI):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'SoftwareInstance',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Software Instance with the given key or criteria """
        return ItopapiPrototype.find(ItopapiSoftwareInstance, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiSoftwareInstance, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Software Instance """
        return ItopapiPrototype.find_all(ItopapiSoftwareInstance)

    """
    ItopapiSoftwareInstance is an object that represents a Software Instance from iTop
    """
    def __init__(self, data=None):
        super(ItopapiSoftwareInstance, self).__init__(data)

# Register as a subclass of FunctionalCI
ItopapiFunctionalCI.register(ItopapiSoftwareInstance)
