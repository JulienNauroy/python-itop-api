# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiNetworkDevice is an abstraction of NetworkDevice representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.datacenterDevice import ItopapiDatacenterDevice
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation
from itopapi.model.features.hasBrand import HasBrand
from itopapi.model.features.hasModel import HasModel
from itopapi.model.features.hasRack import HasRack
from itopapi.model.features.hasEnclosure import HasEnclosure
from itopapi.model.features.hasNetworkDeviceType import HasNetworkDeviceType
from itopapi.model.features.hasIOSVersion import HasIOSVersion
from itopapi.model.features.hasPowerA import HasPowerA
from itopapi.model.features.hasPowerB import HasPowerB

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiNetworkDevice(ItopapiDatacenterDevice, HasOrganization, HasLocation, HasBrand, HasModel,
                       HasRack, HasEnclosure, HasNetworkDeviceType, HasIOSVersion, HasPowerA, HasPowerB):
    """
    ItopapiNetworkDevice is an object that represents a NetworkDevice from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'NetworkDevice',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'managementip',
                 'nb_u', 'serialnumber', 'asset_number', 'move2production',
                 'purchase_date', 'end_of_warranty', 'description', 'ram'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasLocation.foreign_key,
            HasBrand.foreign_key,
            HasModel.foreign_key,
            HasRack.foreign_key,
            HasNetworkDeviceType.foreign_key,
            HasEnclosure.foreign_key,
            HasIOSVersion.foreign_key,
            HasPowerA.foreign_key,
            HasPowerB.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'Person',
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of NetworkDevice with the given key or criteria """
        return ItopapiPrototype.find(ItopapiNetworkDevice, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiNetworkDevice, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of NetworkDevice """
        return ItopapiPrototype.find_all(ItopapiNetworkDevice)

    def __init__(self, data=None):
        super(ItopapiNetworkDevice, self).__init__(data)

        # NetworkDevice's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # NetworkDevice's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        self.managementip = None
        # Rack units
        self.nb_u = None
        # NetworkDevice's serial number
        self.serialnumber = None
        # NetworkDevice's asset number
        self.asset_number = None
        # NetworkDevice's move to production date
        self.move2production = None
        # NetworkDevice's purchase date
        self.purchase_date = None
        # NetworkDevice's end of warranty date
        self.end_of_warranty = None
        # NetworkDevice's description, as a free text
        self.description = None
        # Amount of RAM in the device
        self.ram = None

        ##############################
        #           Lists            #
        ##############################
        # NetworkDevice's softwares list
        self.softwares_list = {}
        # NetworkDevice's contacts list
        self.contacts_list = {}
        # NetworkDevice's documents list
        self.documents_list = {}
        # NetworkDevice's tickets list
        self.tickets_list = {}
        # NetworkDevice's application solutions list
        self.applicationsolution_list = {}
        # NetworkDevice's network interfaces list
        self.physicalinterface_list = {}
        # NetworkDevice's FC ports list
        self.fiberinterfacelist_list = {}
        # NetworkDevice's network devices list
        self.networkdevice_list = {}
        # NetworkDevice's SANs list
        self.san_list = {}
        # NetworkDevice's provider contracts list
        self.providercontracts_list = {}
        # NetworkDevice's services list
        self.services_list = {}
        # ConnectableCI's list
        self.connectablecis_list = {}

# Register as a subclass of Datacenter Device
ItopapiDatacenterDevice.register(ItopapiNetworkDevice)