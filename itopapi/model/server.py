# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiServers is an abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation
from itopapi.model.features.hasBrand import HasBrand
from itopapi.model.features.hasModel import HasModel
from itopapi.model.features.hasOSFamily import HasOSFamily
from itopapi.model.features.hasOSVersion import HasOSVersion
from itopapi.model.features.hasOSLicence import HasOSLicence
from itopapi.model.features.hasRack import HasRack

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiServer(ItopapiPrototype, HasOrganization, HasLocation, HasBrand, HasModel,
                    HasOSFamily, HasOSVersion, HasOSLicence, HasRack):
    """
    ItopapiServers is an object that represents a Servers from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Server',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'managementip',
                 'cpu', 'ram', 'nb_u', 'serialnumber', 'asset_number', 'move2production',
                 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasLocation.foreign_key,
            HasBrand.foreign_key,
            HasModel.foreign_key,
            HasOSFamily.foreign_key,
            HasOSVersion.foreign_key,
            HasOSLicence.foreign_key,
            HasRack.foreign_key,
            {'id': 'enclosure_id', 'name': 'enclosure_name', 'table': 'Enclosure'},
            {'id': 'powerA_id', 'name': 'powerA_name', 'table': 'TODO'},
            {'id': 'powerB_id', 'name': 'powerB_name', 'table': 'TODO'},
        ],
        'list_types': {
            'contacts_list': 'Person',
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of Server with the given key or criteria """
        return ItopapiPrototype.find(ItopapiServer, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiServer, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Server """
        return ItopapiPrototype.find_all(ItopapiServer)

    def __init__(self, data=None):
        super(ItopapiServer, self).__init__(data)

        ##################################
        # Properties/General Information #
        ##################################
        # Server's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # Server's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Server's enclosure (chassis) id. Call findEnclosure to get the full information or just
        # use enclosure_id_friendlyname and enclosure_name
        self.enclosure_id = None
        # Server's enclosure id's friendly name. Not sure the difference with enclosure_name
        self.enclosure_id_friendlyname = None
        # Server's enclosure name
        self.enclosure_name = None

        ##################################
        #  Properties/More Information   #
        ##################################

        self.managementip = None

        self.cpu = None
        self.ram = None
        # Rack units
        self.nb_u = None
        # Server's serial number
        self.serialnumber = None
        # Server's asset number
        self.asset_number = None

        ##################################
        #        Properties/Date         #
        ##################################
        # Server's move to production date
        self.move2production = None
        # Server's purchase date
        self.purchase_date = None
        # Server's end of warranty date
        self.end_of_warranty = None

        ##################################
        #  Properties/Other Information  #
        ##################################
        self.powerA_id = None
        self.powerA_id_finalclass_recall = None
        self.powerA_id_friendlyname = None
        self.powerA_name = None
        self.powerB_id = None
        self.powerB_id_finalclass_recall = None
        self.powerB_id_friendlyname = None
        self.powerB_name = None
        # Server's description, as a free text
        self.description = None

        ##################################
        #           Softwares            #
        ##################################
        # Server's softwares list
        self.softwares_list = {}

        ##################################
        #            Contacts            #
        ##################################
        # Server's contacts list
        self.contacts_list = {}

        ##################################
        #           Documents            #
        ##################################
        # Server's documents list
        self.documents_list = {}

        ##################################
        #            Tickets             #
        ##################################
        # Server's tickets list
        self.tickets_list = {}

        ##################################
        #     Application solutions      #
        ##################################
        # Server's application solutions list
        self.applicationsolution_list = {}

        ##################################
        #       Network interfaces       #
        ##################################
        # Server's network interfaces list
        self.physicalinterface_list = {}

        ##################################
        #            FC ports            #
        ##################################
        # Server's FC ports list
        self.fiberinterfacelist_list = {}

        ##################################
        #        Network devices         #
        ##################################
        # Server's network devices list
        self.networkdevice_list = {}

        ##################################
        #              SANs              #
        ##################################
        # Server's SANs list
        self.san_list = {}

        ##################################
        #        Logical volumes         #
        ##################################
        # Server's logical volumes list
        self.logicalvolumes_list = {}

        ##################################
        #       Provider contracts       #
        ##################################
        # Server's provider contracts list
        self.providercontracts_list = {}

        ##################################
        #            Services            #
        ##################################
        # Server's services list
        self.services_list = {}

    def find_enclosure(self):
        """
        Retrieve the ItopapiEnclosure corresponding to this server
        """
        if self.enclosure_id is not None:
            return ItopapiPrototype.get_itop_class('Enclosure').find(self.enclosure_id)
        return None

    def find_power_a(self):
        """
        Retrieve the ItopapiPowerA corresponding to this server
        """
        if self.powerA_id is not None:
            return ItopapiPrototype.get_itop_class('PowerSource').find(self.powerA_id)
        return None

    def find_power_b(self):
        """
        Retrieve the ItopapiPowerB corresponding to this server
        """
        if self.powerB_id is not None:
            return ItopapiPrototype.get_itop_class('PowerSource').find(self.powerB_id)
        return None
