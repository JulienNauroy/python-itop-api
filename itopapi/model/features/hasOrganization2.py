# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasOrganization2 is a mixin representing the organization attached to some of the objects.
It is only used by ItopaiVLAN which has org_name instead of organization_name
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasOrganization2(object):
    """
    HasOrganization2 represents the Organization attached to some top-level objects.
    It is nearly a duplicate of HasOrganization with org_name instead of organization_name
    because of iTop's poor naming conventions.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'org_id', 'name': 'org_name', 'table': 'Organization'}

    def __init__(self):
        super(HasOrganization2, self).__init__()

        # Object's organization id. Call find_organization to get the full information or just use
        # org_id_friendlyname and organization_name
        self.org_id = None
        # Object's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Object's organization name
        self.org_name = None

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization related to this instance
        """
        if self.org_id is not None:
            return ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None

    def set_organization(self, organization):
        """
        Set the ItopapiOrganization parameters
        """
        self.org_id = organization.instance_id
        self.org_id_friendlyname = organization.friendlyname
        self.org_name = organization.name
