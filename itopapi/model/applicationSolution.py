# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiApplicationSolution is an abstraction of Application Solution representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.functionalCI import ItopapiFunctionalCI
from itopapi.model.features.hasOrganization import HasOrganization


__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiApplicationSolution(ItopapiFunctionalCI, HasOrganization):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'ApplicationSolution',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'move2production', 'description', 'redundancy'],
        'foreign_keys': [
            HasOrganization.foreign_key,
        ],
        'list_types': {
            'functionalcis_list': 'functionalci_id_finalclass_recall',
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiApplicationSolution, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiApplicationSolution, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of ApplicationSolution """
        return ItopapiPrototype.find_all(ItopapiApplicationSolution)

    """
    ItopapiApplicationSolution is an object that represents an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiApplicationSolution, self).__init__(data)
        ##################################
        #           Properties           #
        ##################################
        # Application Solution's status. Values within [inactive, active]
        self.status = None
        # Application Solution's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Application Solution's move to production date
        self.move2production = None
        # Application Solution's description, as a free text
        self.description = None
        self.redundancy = None
        ##################################
        #             Lists              #
        ##################################
        self.functionalcis_list = None
        self.documents_list = None
        self.softwares_list = None
        self.applicationsolution_list = None
        self.tickets_list = None
        self.businessprocess_list = None
        self.services_list = None
        self.contacts_list = None
        self.providercontracts_list = None


# Register as a subclass of FunctionalCI
ItopapiFunctionalCI.register(ItopapiApplicationSolution)
