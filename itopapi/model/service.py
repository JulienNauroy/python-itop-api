# -*- coding: utf8 -*-fr

"""
ItopapiService is a abstraction of Service representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiService(ItopapiPrototype, HasOrganization):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Service',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'description', 'status'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            {'id': 'servicefamily_id', 'name': 'servicefamily_name', 'table': 'ServiceFamily'},
        ],
        'list_types': {
            'functionalcis_list': 'functionalci_id_finalclass_recall',
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiService, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiService, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PhysicalInterface """
        return ItopapiPrototype.find_all(ItopapiService)

    """
    ItopapiService is an object that represents a Service from iTop
    """
    def __init__(self, data=None):
        super(ItopapiService, self).__init__(data)
        # Service Family
        self.servicefamily_id = None
        self.servicefamily_id_friendlyname = None
        self.servicefamily_name = None
        # Description
        self.description = None
        # Service's status. Values within [implementation, obsolete, production]
        self.status = None
        # Lists
        self.servicesubcategories_list = None
        self.documents_list = None
        self.contacts_list = None
        self.customercontracts_list = None
        self.providercontracts_list = None
        self.functionalcis_list = None
