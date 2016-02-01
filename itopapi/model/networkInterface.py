# -*- coding: utf8 -*-fr

"""
ItopapiNetworkInterface is an abstraction of NetworkInterface representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiNetworkInterface(ItopapiPrototype):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'NetworkInterface',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of NetworkInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiNetworkInterface, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiNetworkInterface, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of NetworkInterface """
        return ItopapiPrototype.find_all(ItopapiNetworkInterface)

    """
    ItopapiNetworkInterface is an object that represents a NetworkInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiNetworkInterface, self).__init__(data)
