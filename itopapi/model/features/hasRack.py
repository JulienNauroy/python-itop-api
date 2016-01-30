# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasRack is a mixin representing the rack attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasRack(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'rack_id', 'name': 'rack_name', 'table': 'Rack'}

    def __init__(self):
        super(HasRack, self).__init__()

        # Object's rack id. Call find_rack to get the full information or just use
        # rack_id_friendlyname and rack_name
        self.rack_id = None
        # Object's rack id's friendly name. Not sure the difference with rack_name
        self.rack_id_friendlyname = None
        # Object's rack name
        self.rack_name = None

    def find_rack(self):
        """
        Retrieve the ItopapiRack related to this instance
        """
        if self.rack_id is not None:
            return ItopapiPrototype.get_itop_class('Rack').find(self.rack_id)
        return None

    def set_rack(self, rack):
        """
        Set the ItopapiRack parameters
        """
        self.rack_id = rack.instance_id
        self.rack_id_friendlyname = rack.friendlyname
        self.rack_name = rack.name
