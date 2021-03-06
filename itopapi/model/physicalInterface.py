# -*- coding: utf8 -*-fr

"""
ItopapiPhysicalInterface is an abstraction of PhysicalInterface representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.ipInterface import ItopapiIPInterface
from itopapi.model.features.hasConnectableCI import HasConnectableCI

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPhysicalInterface(ItopapiIPInterface, HasConnectableCI):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'PhysicalInterface',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'ipaddress', 'macaddress', 'comment', 'ipgateway', 'ipmask', 'speed'],
        'foreign_keys': [
            HasConnectableCI.foreign_key,
        ],
        'list_types': {'vlans_list': 'VLAN'},
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPhysicalInterface, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPhysicalInterface, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PhysicalInterface """
        return ItopapiPrototype.find_all(ItopapiPhysicalInterface)

    """
    ItopapiPhysicalInterface is an object that represents a PhysicalInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPhysicalInterface, self).__init__(data)
        # IP address of the PhysicalInterface
        self.ipaddress = None
        # MAC address of the PhysicalInterface
        self.macaddress = None
        # Any kind of comment
        self.comment = None
        # IP gateway of the PhysicalInterface
        self.ipgateway = None
        # IP mask of the PhysicalInterface
        self.ipmask = None
        # speed of the PhysicalInterface
        self.speed = None
        # List of vlans for the PhysicalInterface
        self.vlans_list = None


# Register as a subclass of IPInterface
ItopapiIPInterface.register(ItopapiPhysicalInterface)
