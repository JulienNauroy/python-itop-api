# -*- coding: utf8 -*-fr

"""
ItopapiIPInterface is an abstraction of IPInterface representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.networkInterface import ItopapiNetworkInterface

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiIPInterface(ItopapiNetworkInterface):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'IPInterface',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of IPInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiIPInterface, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiIPInterface, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of IPInterface """
        return ItopapiPrototype.find_all(ItopapiIPInterface)

    """
    ItopapiIPInterface is an object that represents a IPInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiIPInterface, self).__init__(data)


# Register as a subclass of NetworkInterface
ItopapiNetworkInterface.register(ItopapiIPInterface)
