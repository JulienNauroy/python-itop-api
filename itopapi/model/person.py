# -*- coding: utf8 -*-fr

"""
ItopapiPerson is an abstraction of a Person representation on iTop
Note : Person has no finalclass and name. It complicates things...
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPerson(ItopapiPrototype, HasOrganization, HasLocation):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Person',
        # Define which fields to save when creating or updating from the python API
        'save': ['contact_id', 'contact_name', 'function', 'first_name', 'name',
                 'email', 'mobile_phone', 'phone', 'notify', 'employee_number', 'status'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasLocation.foreign_key,
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
        self.manager_id = None,
        self.manager_id_friendlyname = None,
        self.manager_name = None,
        self.function = None
        self.first_name = None
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
