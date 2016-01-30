# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasOSFamily is a mixin representing the osfamily attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasOSFamily(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'osfamily_id', 'name': 'osfamily_name', 'table': 'OSFamily'}

    def __init__(self):
        super(HasOSFamily, self).__init__()

        # Object's osfamily id. Call find_osfamily to get the full information or just use
        # osfamily_id_friendlyname and osfamily_name
        self.osfamily_id = None
        # Object's osfamily id's friendly name. Not sure the difference with osfamily_name
        self.osfamily_id_friendlyname = None
        # Object's osfamily name
        self.osfamily_name = None

    def find_osfamily(self):
        """
        Retrieve the ItopapiOSFamily related to this instance
        """
        if self.osfamily_id is not None:
            return ItopapiPrototype.get_itop_class('OSFamily').find(self.osfamily_id)
        return None

    def set_osfamily(self, osfamily):
        """
        Set the ItopapiOrganization parameters
        """
        self.osfamily_id = osfamily.instance_id
        self.osfamily_id_friendlyname = osfamily.friendlyname
        self.osfamily_name = osfamily.name
