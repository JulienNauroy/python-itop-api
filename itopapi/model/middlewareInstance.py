# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiMiddlewareInstance is an abstraction of Middleware Instance representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.functionalCI import ItopapiFunctionalCI
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasMiddleware import HasMiddleware


__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiMiddlewareInstance(ItopapiFunctionalCI, HasOrganization, HasMiddleware):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'MiddlewareInstance',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'business_criticity', 'move2production', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasMiddleware.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of MiddlewareInstance with the given key or criteria """
        return ItopapiPrototype.find(ItopapiMiddlewareInstance, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiMiddlewareInstance, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of MiddlewareInstance """
        return ItopapiPrototype.find_all(ItopapiMiddlewareInstance)

    """
    ItopapiMiddlewareInstance is an object that represents an Middleware Instance from iTop
    """
    def __init__(self, data=None):
        super(ItopapiMiddlewareInstance, self).__init__(data)
        ##################################
        #           Properties           #
        ##################################
        # Middleware Instance's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Middleware Instance's move to production date
        self.move2production = None
        # Middleware Instance's description, as a free text
        self.description = None
        ##################################
        #             Lists              #
        ##################################
        # One with an s, one without. Because why not?
        self.applicationsolution_list = None
        self.documents_list = None
        self.softwares_list = None
        self.tickets_list = None
        self.services_list = None
        self.contacts_list = None
        self.providercontracts_list = None


# Register as a subclass of FunctionalCI
ItopapiFunctionalCI.register(ItopapiMiddlewareInstance)
