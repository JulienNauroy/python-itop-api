# -*- coding: utf8 -*-fr

"""
ItopapiPerson is a abstraction of a Person representation on iTop
Note : Person has no finalclass and name. It complicates things...
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPerson(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Person',
        # Define which fields to save when creating or updating from the python API
        'save': ['contact_id', 'contact_name', 'function', 'first_name', 'name',
                 'email', 'mobile_phone', 'phone', 'notify', 'employee_number', 'status'],
        'foreign_keys': [
            {'id': 'location_id', 'name': 'location_name', 'table': 'Location'},
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'manager_id', 'name': 'manager_name', 'table': 'Person'},
        ],
        'list_types': {
            'team_list': 'Team',
            'cis_list': 'functionalci_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPerson, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPerson, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Person """
        return ItopapiPrototype.find_all(ItopapiPerson)

    """
    ItopapiPerson is an object that represents a Person from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPerson, self).__init__(data)
        ##################################
        #           Properties           #
        ##################################
        self.contact_id = None
        self.contact_name = None
        # Person's location id. Call find_location to get the full information or just use
        # location_id_friendlyname and location_name
        self.location_id = None
        # Person's location id's friendly name. Not sure the difference with location_name
        self.location_id_friendlyname = None
        # Person's location name
        self.location_name = None
        # Person's organization id. Call find_organization to get the full information or just use
        #  org_id_friendlyname and organization_name
        self.org_id = None
        # Person's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        self.manager_id = None,
        self.manager_id_friendlyname = None,
        self.manager_name = None,
        # Person's organization name
        self.organization_name = None
        self.function = None
        self.first_name = None
        self.name = None
        self.email = None
        self.mobile_phone = None
        self.phone = None
        self.organization_name = None
        self.notify = None
        self.employee_number = None
        self.organization_name = None
        self.status = None
        ##################################
        #             Lists              #
        ##################################
        self.tickets_list = None
        self.tickets_list = None
        self.tickets_list = None

    def find_location(self):
        """
        Retrieve the ItopapiLocation related to this instance
        """
        if self.location_id is not None:
            ItopapiPrototype.get_itop_class('Location').find(self.location_id)
        return None

    def find_organization(self):
        """
        Retrieve the parent ItopapiOrganization
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None
