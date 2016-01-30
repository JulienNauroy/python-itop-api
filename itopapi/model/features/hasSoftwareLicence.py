# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasSoftwareLicence is a mixin representing the softwarelicence attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasSoftwareLicence(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'softwarelicence_id', 'name': 'softwarelicence_name', 'table': 'SoftwareLicence'}

    def __init__(self):
        super(HasSoftwareLicence, self).__init__()

        # Object's softwarelicence id. Call find_softwarelicence to get the full information or just use
        # softwarelicence_id_friendlyname and softwarelicence_name
        self.softwarelicence_id = None
        # Object's softwarelicence id's friendly name. Not sure the difference with softwarelicence_name
        self.softwarelicence_id_friendlyname = None
        # Object's softwarelicence name
        self.softwarelicence_name = None

    def find_softwarelicence(self):
        """
        Retrieve the ItopapiSoftwareLicence related to this instance
        """
        if self.softwarelicence_id is not None:
            return ItopapiPrototype.get_itop_class('SoftwareLicence').find(self.softwarelicence_id)
        return None

    def set_softwarelicence(self, softwarelicence):
        """
        Set the ItopapiOrganization parameters
        """
        self.softwarelicence_id = softwarelicence.instance_id
        self.softwarelicence_id_friendlyname = softwarelicence.friendlyname
        self.softwarelicence_name = softwarelicence.name
