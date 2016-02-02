# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasParentOrganization is a mixin representing the parent organization attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasParentOrganization(object):
    """
    HasParentOrganization represents the ParentOrganization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'parent_id', 'name': 'parent_name', 'table': 'Organization'}

    def __init__(self):
        super(HasParentOrganization, self).__init__()

        # Object's parent id. Call find_parent to get the full information or just use
        # parent_id_friendlyname and parent_name
        self.parent_id = None
        # Object's parent id's friendly name. Not sure the difference with parent_name
        self.parent_id_friendlyname = None
        # Object's parent name
        self.parent_name = None

    def find_parent(self):
        """
        Retrieve the ItopapiOrganization related to this instance
        """
        if self.parent_id is not None:
            return ItopapiPrototype.get_itop_class('Organization').find(self.parent_id)
        return None

    def set_parent(self, parent):
        """
        Set the ItopapiOrganization parameters
        """
        self.parent_id = parent.instance_id
        self.parent_id_friendlyname = parent.friendlyname
        self.parent_name = parent.name
