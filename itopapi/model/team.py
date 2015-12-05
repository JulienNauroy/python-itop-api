# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
ItopapiTeam is a abstraction of Team representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiTeam(ItopapiPrototype):
    """
    ItopapiTeam is a object that represents a Team from iTop
    """

    """ Configuration specific to itop """
    itop = {
        # Name of the class in Itop
        'name': 'Team',
        # Define which fields to save when creating or updating from the python API
        'save': ['status', 'phone', 'notify', 'name', 'function', 'email'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
        ],
        'list_types': {
            'persons_list': 'Person',
            'cis_list': 'functionalci_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Team with the given key or criteria """
        return ItopapiPrototype.find(ItopapiTeam, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiTeam, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Rack """
        return ItopapiPrototype.find_all(ItopapiTeam)

    def __init__(self, data=None):
        super(ItopapiTeam, self).__init__(data)

        ##################################
        #           Properties           #
        ##################################
        # Team's organization id. Call find_organization to get the full information or just use
        # org_id_friendlyname and organization_name
        self.org_id = None
        # Team's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Team's organization name
        self.organization_name = None
        self.status = None
        self.phone = None
        self.notify = None
        self.name = None
        self.function = None
        self.email = None
        ##################################
        #             Lists              #
        ##################################
        self.cis_list = None
        self.tickets_list = None
        self.persons_list = None

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization related to this instance
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None
