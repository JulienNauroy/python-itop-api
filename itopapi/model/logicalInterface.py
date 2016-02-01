# -*- coding: utf8 -*-fr

"""
ItopapiLogicalInterface is an abstraction of LogicalInterface representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.ipInterface import ItopapiIPInterface
from itopapi.model.features.hasVirtualMachine import HasVirtualMachine

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiLogicalInterface(ItopapiIPInterface, HasVirtualMachine):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'LogicalInterface',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'ipaddress', 'macaddress', 'comment', 'ipgateway', 'ipmask', 'speed'],
        'foreign_keys': [
            HasVirtualMachine.foreign_key,
        ],
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of LogicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiLogicalInterface, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiLogicalInterface, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of LogicalInterface """
        return ItopapiPrototype.find_all(ItopapiLogicalInterface)

    """
    ItopapiLogicalInterface is an object that represents a LogicalInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiLogicalInterface, self).__init__(data)
        # IP address of the LogicalInterface
        self.ipaddress = None
        # MAC address of the LogicalInterface
        self.macaddress = None
        # Any kind of comment
        self.comment = None
        # IP gateway of the LogicalInterface
        self.ipgateway = None
        # IP mask of the LogicalInterface
        self.ipmask = None
        # speed of the LogicalInterface
        self.speed = None


# Register as a subclass of IPInterface
ItopapiIPInterface.register(ItopapiLogicalInterface)
