# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasLocation is a mixin representing the location attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasLocation(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'location_id', 'name': 'location_name', 'table': 'Location'}

    def __init__(self):
        super(HasLocation, self).__init__()

        # Object's location id. Call find_location to get the full information or just use
        # location_id_friendlyname and location_name
        self.location_id = None
        # Object's location id's friendly name. Not sure the difference with location_name
        self.location_id_friendlyname = None
        # Object's location name
        self.location_name = None

    def find_location(self):
        """
        Retrieve the ItopapiLocation related to this instance
        """
        if self.location_id is not None:
            return ItopapiPrototype.get_itop_class('Location').find(self.location_id)
        return None

    def set_location(self, location):
        """
        Set the ItopapiOrganization parameters
        """
        self.location_id = location.instance_id
        self.location_id_friendlyname = location.friendlyname
        self.location_name = location.name
