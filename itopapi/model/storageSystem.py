# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiStorageSystem is an abstraction of StorageSystem representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.datacenterDevice import ItopapiDatacenterDevice
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation
from itopapi.model.features.hasBrand import HasBrand
from itopapi.model.features.hasModel import HasModel
from itopapi.model.features.hasRack import HasRack
from itopapi.model.features.hasEnclosure import HasEnclosure
from itopapi.model.features.hasPowerA import HasPowerA
from itopapi.model.features.hasPowerB import HasPowerB

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiStorageSystem(ItopapiDatacenterDevice, HasOrganization, HasLocation, HasBrand, HasModel,
                       HasRack, HasEnclosure, HasPowerA, HasPowerB):
    """
    ItopapiStorageSystem is an object that represents a StorageSystem from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'StorageSystem',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'managementip',
                 'nb_u', 'serialnumber', 'asset_number', 'move2production',
                 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasLocation.foreign_key,
            HasBrand.foreign_key,
            HasModel.foreign_key,
            HasRack.foreign_key,
            HasEnclosure.foreign_key,
            HasPowerA.foreign_key,
            HasPowerB.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'Person',
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or mor instance of StorageSystem with the given key or criteria """
        return ItopapiPrototype.find(ItopapiStorageSystem, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiStorageSystem, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of StorageSystem """
        return ItopapiPrototype.find_all(ItopapiStorageSystem)

    def __init__(self, data=None):
        super(ItopapiStorageSystem, self).__init__(data)

        # StorageSystem's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # StorageSystem's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        self.managementip = None
        # Rack units
        self.nb_u = None
        # StorageSystem's serial number
        self.serialnumber = None
        # StorageSystem's asset number
        self.asset_number = None
        # StorageSystem's move to production date
        self.move2production = None
        # StorageSystem's purchase date
        self.purchase_date = None
        # StorageSystem's end of warranty date
        self.end_of_warranty = None
        # StorageSystem's description, as a free text
        self.description = None

        ##############################
        #           Lists            #
        ##############################
        # StorageSystem's softwares list
        self.softwares_list = {}
        # StorageSystem's contacts list
        self.contacts_list = {}
        # StorageSystem's documents list
        self.documents_list = {}
        # StorageSystem's tickets list
        self.tickets_list = {}
        # StorageSystem's application solutions list
        self.applicationsolution_list = {}
        # StorageSystem's network interfaces list
        self.physicalinterface_list = {}
        # StorageSystem's FC ports list
        self.fiberinterfacelist_list = {}
        # StorageSystem's network devices list
        self.networkdevice_list = {}
        # StorageSystem's SANs list
        self.san_list = {}
        # StorageSystem's provider contracts list
        self.providercontracts_list = {}
        # StorageSystem's services list
        self.services_list = {}
        # LogicalVolume's list
        self.logicalvolume_list = {}

# Register as a subclass of Datacenter Device
ItopapiDatacenterDevice.register(ItopapiStorageSystem)