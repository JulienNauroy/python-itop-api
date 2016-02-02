# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiNAS is an abstraction of NAS representation on iTop
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


class ItopapiNAS(ItopapiDatacenterDevice, HasOrganization, HasLocation, HasBrand, HasModel,
                       HasRack, HasEnclosure, HasPowerA, HasPowerB):
    """
    ItopapiNAS is an object that represents a NAS from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'NAS',
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
        """ Retrieve one or mor instance of NAS with the given key or criteria """
        return ItopapiPrototype.find(ItopapiNAS, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiNAS, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of NAS """
        return ItopapiPrototype.find_all(ItopapiNAS)

    def __init__(self, data=None):
        super(ItopapiNAS, self).__init__(data)

        # NAS's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # NAS's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        self.managementip = None
        # Rack units
        self.nb_u = None
        # NAS's serial number
        self.serialnumber = None
        # NAS's asset number
        self.asset_number = None
        # NAS's move to production date
        self.move2production = None
        # NAS's purchase date
        self.purchase_date = None
        # NAS's end of warranty date
        self.end_of_warranty = None
        # NAS's description, as a free text
        self.description = None

        ##############################
        #           Lists            #
        ##############################
        # NAS's softwares list
        self.softwares_list = {}
        # NAS's contacts list
        self.contacts_list = {}
        # NAS's documents list
        self.documents_list = {}
        # NAS's tickets list
        self.tickets_list = {}
        # NAS's application solutions list
        self.applicationsolution_list = {}
        # NAS's network interfaces list
        self.physicalinterface_list = {}
        # NAS's FC ports list
        self.fiberinterfacelist_list = {}
        # NAS's network devices list
        self.networkdevice_list = {}
        # NAS's SANs list
        self.san_list = {}
        # NAS's provider contracts list
        self.providercontracts_list = {}
        # NAS's services list
        self.services_list = {}
        # NASFileSystem's list
        self.nasfilesystem_list = {}

# Register as a subclass of Datacenter Device
ItopapiDatacenterDevice.register(ItopapiNAS)