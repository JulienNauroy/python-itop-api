# -*- coding: utf8 -*-fr

"""
ItopapiHypervisor is a abstraction of a virtual servers Hypervisor representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiHypervisor(ItopapiPrototype, HasOrganization):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Hypervisor',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'move2production', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            {'id': 'server_id', 'name': 'server_name', 'table': 'Server'},
            {'id': 'farm_id', 'name': 'farm_name', 'table': 'Farm'},
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Hypervisor with the given key or criteria """
        return ItopapiPrototype.find(ItopapiHypervisor, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiHypervisor, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Hypervisor """
        return ItopapiPrototype.find_all(ItopapiHypervisor)

    """
    ItopapiHypervisor is an object that represents a Hypervisor from iTop
    """
    def __init__(self, data=None):
        super(ItopapiHypervisor, self).__init__(data)
        # Hypervisor's status. Values within [inactive, active]
        self.status = None
        # Hypervisor's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Hypervisor's move to production date
        self.move2production = None
        # Hypervisor's description, as a free text
        self.description = None
        # Physical server the hypervisor is running onto
        self.server_id = None
        self.server_id_friendlyname = None
        self.server_name = None
        # Farm the hypervisor belongs to
        self.farm_id = None
        self.farm_id_friendlyname = None
        self.farm_name = None

        # Lists
        self.tickets_list = None
        self.providercontracts_list = None
        self.virtualmachine_list = None
        self.services_list = None
        self.applicationsolution_list = None
        self.softwares_list = None
        self.documents_list = None
        self.contacts_list = None
        self.logicalvolumes_list = None
