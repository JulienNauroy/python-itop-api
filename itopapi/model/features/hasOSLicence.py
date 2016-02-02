# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasOSLicence is a mixin representing the oslicence attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasOSLicence(object):
    """
    HasOSLicence represents the OSLicence attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'oslicence_id', 'name': 'oslicence_name', 'table': 'OSLicence'}

    def __init__(self):
        super(HasOSLicence, self).__init__()

        # Object's oslicence id. Call find_oslicence to get the full information or just use
        # oslicence_id_friendlyname and oslicence_name
        self.oslicence_id = None
        # Object's oslicence id's friendly name. Not sure the difference with oslicence_name
        self.oslicence_id_friendlyname = None
        # Object's oslicence name
        self.oslicence_name = None

    def find_oslicence(self):
        """
        Retrieve the ItopapiOSLicence related to this instance
        """
        if self.oslicence_id is not None:
            return ItopapiPrototype.get_itop_class('OSLicence').find(self.oslicence_id)
        return None

    def set_oslicence(self, oslicence):
        """
        Set the ItopapiOSlicence parameters
        """
        self.oslicence_id = oslicence.instance_id
        self.oslicence_id_friendlyname = oslicence.friendlyname
        self.oslicence_name = oslicence.name
