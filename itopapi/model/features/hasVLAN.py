# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasVLAN is a mixin representing the VLAN attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasVLAN(object):
    """
    HasVLAN represents the VLAN attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'vlan_id', 'name': 'vlan_tag', 'table': 'Person'}

    def __init__(self):
        super(HasVLAN, self).__init__()

        # Object's vlan id. Call find_vlan to get the full information or just use vlan_name
        self.vlan_id = None
        # Object's vlan id's friendly name. Not sure the difference with vlan_name
        self.vlan_id_friendlyname = None
        # Object's vlan name
        self.vlan_name = None

    def find_vlan(self):
        """
        Retrieve the ItopapiVLAN related to this instance
        """
        if self.vlan_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.vlan_id)
        return None

    def set_vlan(self, vlan):
        """
        Set the ItopapiPerson parameters
        """
        self.vlan_id = vlan.instance_id
        self.vlan_id_friendlyname = vlan.friendlyname
        self.vlan_name = vlan.name
