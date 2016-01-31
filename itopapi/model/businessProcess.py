# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiBusinessProcess is an abstraction of Business Process representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.functionalCI import ItopapiFunctionalCI
from itopapi.model.features.hasOrganization import HasOrganization


__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiBusinessProcess(ItopapiFunctionalCI, HasOrganization):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'BusinessProcess',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'move2production', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of BusinessProcess with the given key or criteria """
        return ItopapiPrototype.find(ItopapiBusinessProcess, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiBusinessProcess, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of BusinessProcess """
        return ItopapiPrototype.find_all(ItopapiBusinessProcess)

    """
    ItopapiBusinessProcess is an object that represents an Business Process from iTop
    """
    def __init__(self, data=None):
        super(ItopapiBusinessProcess, self).__init__(data)
        ##################################
        #           Properties           #
        ##################################
        # Business Process's status. Values within [inactive, active]
        self.status = None
        # Business Process's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Business Process's move to production date
        self.move2production = None
        # Business Process's description, as a free text
        self.description = None
        ##################################
        #             Lists              #
        ##################################
        # One with an s, one without. Because why not?
        self.applicationsolution_list = None
        self.applicationsolutions_list = None
        self.documents_list = None
        self.softwares_list = None
        self.tickets_list = None
        self.services_list = None
        self.contacts_list = None
        self.providercontracts_list = None


# Register as a subclass of FunctionalCI
ItopapiFunctionalCI.register(ItopapiBusinessProcess)
