# -*- coding: utf8 -*-fr

"""
ItopapiFarm is an abstraction of a virtual servers farm representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiFarm(ItopapiPrototype, HasOrganization):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Farm',
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
        """ Retrieve one or more instance of Farm with the given key or criteria """
        return ItopapiPrototype.find(ItopapiFarm, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiFarm, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Farm """
        return ItopapiPrototype.find_all(ItopapiFarm)

    """
    ItopapiFarm is an object that represents a Farm from iTop
    """
    def __init__(self, data=None):
        super(ItopapiFarm, self).__init__(data)
        # Farm's status. Values within [inactive, active]
        self.status = None
        # Farm's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Farm's move to production date
        self.move2production = None
        # Farm's description, as a free text
        self.description = None
        ##################################
        #             Lists              #
        ##################################
        self.documents_list = None
        self.softwares_list = None
        self.applicationsolution_list = None
        self.tickets_list = None
        self.services_list = None
        self.logicalvolumes_list = None
        self.hypervisor_list = None
        self.virtualmachine_list = None