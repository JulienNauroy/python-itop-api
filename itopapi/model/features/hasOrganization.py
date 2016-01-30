# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasOrganization is a mixin representing the organization attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasOrganization(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'}

    def __init__(self):
        super(HasOrganization, self).__init__()
        # Object's organization id. Call find_organization to get the full information or just use
        # org_id_friendlyname and organization_name
        self.org_id = None
        # Object's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Object's organization name
        self.organization_name = None

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
        self.organization_name = organization.name
