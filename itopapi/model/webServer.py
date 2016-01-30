# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiWebServer is an abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype, ItopapiUnimplementedMethod
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasSoftwareLicence import HasSoftwareLicence

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiWebServer(ItopapiPrototype, HasOrganization, HasSoftwareLicence):
    """
    ItopapiWebServer is an object that represents a WebServer from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'WebServer',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'path', 'move2production', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            {'id': 'system_id', 'name': 'system_id_friendlyname', 'table': 'Server'},
            {'id': 'software_id', 'name': 'software_name', 'table': 'Software'},
            HasSoftwareLicence.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of WebServer with the given key or criteria """
        return ItopapiPrototype.find(ItopapiWebServer, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiWebServer, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of WebServer """
        return ItopapiPrototype.find_all(ItopapiWebServer)

    def __init__(self, data=None):
        super(ItopapiWebServer, self).__init__(data)

        ##################################
        # Properties/General Information #
        ##################################
        # WebServer's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # WebServer's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # System containing the WebServer
        self.system_id = None
        self.system_id_finalclass_recall = None
        self.system_id_friendlyname = None
        self.system_name = None
        # Web server's software
        self.software_id = None
        self.software_id_friendlyname = None
        self.software_name = None
        # Web server's path ?
        self.path = None
        # WebServer's move to production date
        self.move2production = None
        # WebServer's description, as a free text
        self.description = None

        ###############################
        #            Lists            #
        ###############################
        # WebServer's contacts list
        self.contacts_list = {}
        # WebServer's documents list
        self.documents_list = {}
        # WebServer's tickets list
        self.tickets_list = {}
        # WebServer's application solutions list
        self.applicationsolution_list = {}
        # WebServer's web applications list
        self.webapp_list = {}
        # WebServer's network interfaces list
        self.physicalinterface_list = {}
        # WebServer's FC ports list
        self.fiberinterfacelist_list = {}
        # WebServer's network devices list
        self.networkdevice_list = {}
        # WebServer's SANs list
        self.san_list = {}
        # WebServer's logical volumes list
        self.logicalvolumes_list = {}
        # WebServer's provider contracts list
        self.providercontracts_list = {}
        # WebServer's services list
        self.services_list = {}

    def find_system(self):
        """
        Retrieve the System (Server or VirtualMachine) corresponding to this WebServer
        """
        if self.system_id is not None:
            # TODO define System
            raise ItopapiUnimplementedMethod()
        return None

    def find_software(self):
        """
        Retrieve the Software corresponding to this WebServer
        """
        if self.software_id is not None:
            # TODO define Software
            raise ItopapiUnimplementedMethod()
        return None
