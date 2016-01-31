# -*- coding: utf8 -*-fr

"""
ItopapiPerson is an abstraction of a Person representation on iTop
It inherits from ItopapiContact
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.contact import ItopapiContact
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation
from itopapi.model.features.hasManager import HasManager

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPerson(ItopapiContact, HasOrganization, HasLocation, HasManager):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Person',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'contact_id', 'contact_name', 'function', 'first_name',
                 'email', 'mobile_phone', 'phone', 'notify', 'employee_number', 'status'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasLocation.foreign_key,
            HasManager.foreign_key,
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
        self.first_name = None
        self.function = None
        self.email = None
        self.mobile_phone = None
        self.phone = None
        self.notify = None
        self.employee_number = None
        self.status = None
        ##################################
        #             Lists              #
        ##################################
        self.tickets_list = None
        self.cis_list = None
        self.team_list = None

# Register as a subclass of Contact
ItopapiContact.register(ItopapiPerson)
