# -*- coding: utf8 -*-fr

"""
ItopapiVirtualMachine is an abstraction of VLAN representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasOSFamily import HasOSFamily
from itopapi.model.features.hasOSVersion import HasOSVersion
from itopapi.model.features.hasOSLicence import HasOSLicence

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiVirtualMachine(ItopapiPrototype, HasOrganization, HasOSFamily, HasOSVersion, HasOSLicence):

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
            {'id': 'virtualhost_id', 'name': 'virtualhost_name', 'table': 'VirtualHost'},
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

        ##################################
        # Properties/General Information #
        ##################################
        # VirtualMachine's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # VirtualMachine's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # VirtualMachine's virtual host
        self.virtualhost_id = None
        self.virtualhost_id_finalclass_recall = None
        self.virtualhost_id_friendlyname = None
        self.virtualhost_name = None

        ##################################
        #  Properties/More Information   #
        ##################################

        self.managementip = None

        self.cpu = None
        self.ram = None

        ##################################
        #        Properties/Date         #
        ##################################

        ##################################
        #  Properties/Other Information  #
        ##################################
        # VirtualMachine's move to production date
        self.move2production = None
        # VirtualMachine's description, as a free text
        self.description = None

        ##################################
        #           Softwares            #
        ##################################
        # VirtualMachine's softwares list
        self.softwares_list = {}

        ##################################
        #            Contacts            #
        ##################################
        # VirtualMachine's contacts list
        self.contacts_list = {}

        ##################################
        #           Documents            #
        ##################################
        # VirtualMachine's documents list
        self.documents_list = {}

        ##################################
        #            Tickets             #
        ##################################
        # VirtualMachine's tickets list
        self.tickets_list = {}

        ##################################
        #     Application solutions      #
        ##################################
        # VirtualMachine's application solutions list
        self.applicationsolution_list = {}

        ##################################
        #       Network interfaces       #
        ##################################
        # VirtualMachine's network interfaces list
        self.physicalinterface_list = {}

        ##################################
        #        Logical volumes         #
        ##################################
        # VirtualMachine's logical volumes list
        self.logicalvolumes_list = {}

        ##################################
        #       Provider contracts       #
        ##################################
        # VirtualMachine's provider contracts list
        self.providercontracts_list = {}

        ##################################
        #            Services            #
        ##################################
        # VirtualMachine's services list
        self.services_list = {}
