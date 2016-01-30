# -*- coding: utf8 -*-fr

"""
ItopapiVLAN is a abstraction of VLAN representation on iTop
Note : VLAN has no finalclass and name. It complicates things...
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization2 import HasOrganization2

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiVLAN(ItopapiPrototype, HasOrganization2):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'VLAN',
        # Define which fields to save when creating or updating from the python API
        'save': ['vlan_tag', 'description'],
        'foreign_keys': [
            HasOrganization2.foreign_key
        ],
        'list_types': {'physicalinterfaces_list': 'PhysicalInterface', 'subnets_list': 'Subnet'},
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of VLAN with the given key or criteria """
        return ItopapiPrototype.find(ItopapiVLAN, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiVLAN, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of VLAN """
        return ItopapiPrototype.find_all(ItopapiVLAN)

    """
    ItopapiVLAN is an object that represents a VLAN from iTop
    """
    def __init__(self, data=None):
        super(ItopapiVLAN, self).__init__(data)
        # VLAN tag, replaces the "name" value for other classes
        self.vlan_tag = None
        # VLAN's description
        self.description = None
        # Interfaces
        self.physicalinterfaces_list = None
        # subnets
        self.subnets_list = None
