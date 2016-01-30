# -*- coding: utf8 -*-fr

"""
ItopapiVirtualMachine is an abstraction of VLAN representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasOSFamily import HasOSFamily
from itopapi.model.features.hasOSVersion import HasOSVersion
from itopapi.model.features.hasOSLicence import HasOSLicence
from itopapi.model.features.hasVirtualHost import HasVirtualHost

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiVirtualMachine(ItopapiPrototype, HasOrganization, HasOSFamily, HasOSVersion, HasOSLicence, HasVirtualHost):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'VirtualMachine',
        'save': ['name', 'status', 'business_criticity',
                 'managementip', 'oslicence_id', 'cpu', 'ram', 'move2production',
                 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasOSFamily.foreign_key,
            HasOSVersion.foreign_key,
            HasOSLicence.foreign_key,
            HasVirtualHost.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiVirtualMachine, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiVirtualMachine, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PhysicalInterface """
        return ItopapiPrototype.find_all(ItopapiVirtualMachine)

    """
    ItopapiPhysicalInterface is an object that represents a PhysicalInterface from iTop
    """
    def __init__(self, data=None):
        super(ItopapiVirtualMachine, self).__init__(data)

        # VirtualMachine's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # VirtualMachine's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        self.managementip = None
        self.cpu = None
        self.ram = None
        # VirtualMachine's move to production date
        self.move2production = None
        # VirtualMachine's description, as a free text
        self.description = None

        ##############################
        #           Lists            #
        ##############################
        # VirtualMachine's softwares list
        self.softwares_list = {}
        # VirtualMachine's contacts list
        self.contacts_list = {}
        # VirtualMachine's documents list
        self.documents_list = {}
        # VirtualMachine's tickets list
        self.tickets_list = {}
        # VirtualMachine's application solutions list
        self.applicationsolution_list = {}
        # VirtualMachine's network interfaces list
        self.physicalinterface_list = {}
        # VirtualMachine's logical volumes list
        self.logicalvolumes_list = {}
        # VirtualMachine's provider contracts list
        self.providercontracts_list = {}
        # VirtualMachine's services list
        self.services_list = {}
