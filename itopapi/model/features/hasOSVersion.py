# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasOSVersion is a mixin representing the osversion attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasOSVersion(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'osversion_id', 'name': 'osversion_name', 'table': 'OSVersion'}

    def __init__(self):
        super(HasOSVersion, self).__init__()

        # Object's osversion id. Call find_osversion to get the full information or just use
        # osversion_id_friendlyname and osversion_name
        self.osversion_id = None
        # Object's osversion id's friendly name. Not sure the difference with osversion_name
        self.osversion_id_friendlyname = None
        # Object's osversion name
        self.osversion_name = None

    def find_osversion(self):
        """
        Retrieve the ItopapiOSVersion related to this instance
        """
        if self.osversion_id is not None:
            return ItopapiPrototype.get_itop_class('OSVersion').find(self.osversion_id)
        return None

    def set_osversion(self, osversion):
        """
        Set the ItopapiOrganization parameters
        """
        self.osversion_id = osversion.instance_id
        self.osversion_id_friendlyname = osversion.friendlyname
        self.osversion_name = osversion.name
