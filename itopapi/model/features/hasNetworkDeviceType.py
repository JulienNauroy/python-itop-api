# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasNetworkDeviceType is a mixin representing the NetworkDeviceType attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasNetworkDeviceType(object):
    """
    HasNetworkDeviceType represents the NetworkDeviceType attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'networkdevicetype_id', 'name': 'networkdevicetype_name', 'table': 'NetworkDeviceType'}

    def __init__(self):
        super(HasNetworkDeviceType, self).__init__()

        # Object's NetworkDeviceType id. Call find_NetworkDeviceType to get the full information or just use
        # networkdevicetype_id_friendlyname and networkdevicetype_name
        self.networkdevicetype_id = None
        # Object's NetworkDeviceType id's friendly name. Not sure the difference with networkdevicetype_name
        self.networkdevicetype_id_friendlyname = None
        # Object's NetworkDeviceType name
        self.networkdevicetype_name = None

    def find_NetworkDeviceType(self):
        """
        Retrieve the ItopapiNetworkDeviceType related to this instance
        """
        if self.networkdevicetype_id is not None:
            return ItopapiPrototype.get_itop_class('NetworkDeviceType').find(self.networkdevicetype_id)
        return None

    def set_NetworkDeviceType(self, NetworkDeviceType):
        """
        Set the ItopapiNetworkDeviceType parameters
        """
        self.networkdevicetype_id = NetworkDeviceType.instance_id
        self.networkdevicetype_id_friendlyname = NetworkDeviceType.friendlyname
        self.networkdevicetype_name = NetworkDeviceType.name
