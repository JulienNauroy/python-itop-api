# -*- coding: utf8 -*-fr

"""
ItopapiFiberChannelInterface is an abstraction of FiberChannelInterface representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.ipInterface import ItopapiIPInterface
from itopapi.model.features.hasDatacenterDevice import HasDatacenterDevice

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiFiberChannelInterface(ItopapiIPInterface):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'FiberChannelInterface',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'ipaddress', 'macaddress', 'comment', 'ipgateway', 'ipmask', 'speed'],
        'foreign_keys': [
            HasDatacenterDevice.foreign_key,
        ],
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of FiberChannelInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiFiberChannelInterface, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiFiberChannelInterface, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of FiberChannelInterface """
        return ItopapiPrototype.find_all(ItopapiFiberChannelInterface)

    """
    ItopapiFiberChannelInterface is an object that represents a FiberChannelInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiFiberChannelInterface, self).__init__(data)
        # IP address of the FiberChannelInterface
        self.ipaddress = None
        # MAC address of the FiberChannelInterface
        self.macaddress = None
        # Any kind of comment
        self.comment = None
        # IP gateway of the FiberChannelInterface
        self.ipgateway = None
        # IP mask of the FiberChannelInterface
        self.ipmask = None
        # speed of the FiberChannelInterface
        self.speed = None


# Register as a subclass of IPInterface
ItopapiIPInterface.register(ItopapiFiberChannelInterface)
