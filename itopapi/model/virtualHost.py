# -*- coding: utf8 -*-fr

"""
ItopapiVirtualHost is an abstraction of VirtualHost representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.virtualDevice import ItopapiVirtualDevice
from itopapi.model.functionalCI import ItopapiFunctionalCI

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiVirtualHost(ItopapiVirtualDevice):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'VirtualHost',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of VirtualHost with the given key or criteria """
        return ItopapiPrototype.find(ItopapiVirtualHost, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiVirtualHost, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of VirtualHost """
        return ItopapiPrototype.find_all(ItopapiVirtualHost)

    """
    ItopapiVirtualHost is an object that represents a VirtualHost from iTop
    """
    def __init__(self, data=None):
        super(ItopapiVirtualHost, self).__init__(data)


# Register as a subclass of VirtualDevice
ItopapiVirtualDevice.register(ItopapiVirtualHost)
