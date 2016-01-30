# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasSoftware is a mixin representing the software attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasSoftware(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'software_id', 'name': 'software_name', 'table': 'Software'}

    def __init__(self):
        super(HasSoftware, self).__init__()

        # Object's software id. Call find_software to get the full information or just use
        # software_id_friendlyname and software_name
        self.software_id = None
        # Object's software id's friendly name. Not sure the difference with software_name
        self.software_id_friendlyname = None
        # Object's software name
        self.software_name = None

    def find_software(self):
        """
        Retrieve the ItopapiSoftware related to this instance
        """
        if self.software_id is not None:
            return ItopapiPrototype.get_itop_class('Software').find(self.software_id)
        return None

    def set_software(self, software):
        """
        Set the ItopapiServer parameters
        """
        self.software_id = software.instance_id
        self.software_id_friendlyname = software.friendlyname
        self.software_name = software.name
