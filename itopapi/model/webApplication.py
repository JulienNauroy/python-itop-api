# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiWebApplication is an abstraction of WebApplication representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.functionalCI import ItopapiFunctionalCI
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasWebServer import HasWebServer

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiWebApplication(ItopapiFunctionalCI, HasOrganization, HasWebServer):
    """
    ItopapiWebApplication is an object that represents a WebApplication from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'WebApplication',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'url', 'business_criticity', 'move2production', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasWebServer.foreign_key,
        ],
        'list_types': {
            'services_list': 'Service',
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of WebApplication with the given key or criteria """
        return ItopapiPrototype.find(ItopapiWebApplication, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiWebApplication, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of WebApplication """
        return ItopapiPrototype.find_all(ItopapiWebApplication)

    def __init__(self, data=None):
        super(ItopapiWebApplication, self).__init__(data)

        ##################################
        # Properties/General Information #
        ##################################
        # WebApplication's URL
        self.url = None
        # WebApplication's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # WebApplication's move to production date
        self.move2production = None
        # WebApplication's description, as a free text
        self.description = None

        ##################################
        #            Contacts            #
        ##################################
        # WebApplication's contacts list
        self.contacts_list = {}

        ##################################
        #           Documents            #
        ##################################
        # WebApplication's documents list
        self.documents_list = {}

        ##################################
        #            Tickets             #
        ##################################
        # WebApplication's tickets list
        self.tickets_list = {}

        ##################################
        #     Application solutions      #
        ##################################
        # WebApplication's application solutions list
        self.applicationsolution_list = {}

        ##################################
        #       Provider contracts       #
        ##################################
        # WebApplication's provider contracts list
        self.providercontracts_list = {}

        ##################################
        #            Services            #
        ##################################
        # WebApplication's services list
        self.services_list = {}


# Register as a subclass of FunctionalCI
ItopapiFunctionalCI.register(ItopapiWebApplication)
