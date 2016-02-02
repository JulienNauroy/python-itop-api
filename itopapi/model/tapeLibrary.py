# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes,invalid-name, too-many-statements
"""
ItopapiTapeLibrarys is an abstraction of TapeLibrary representation on iTop
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


class ItopapiTapeLibrary(ItopapiDatacenterDevice, HasOrganization, HasLocation, HasBrand, HasModel,
                       HasRack, HasEnclosure, HasPowerA, HasPowerB):
    """
    ItopapiTapeLibrary is an object that represents a TapeLibrary from iTop
    """

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'TapeLibrary',
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
        """ Retrieve one or mor instance of TapeLibrary with the given key or criteria """
        return ItopapiPrototype.find(ItopapiTapeLibrary, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiTapeLibrary, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of TapeLibrary """
        return ItopapiPrototype.find_all(ItopapiTapeLibrary)

    def __init__(self, data=None):
        super(ItopapiTapeLibrary, self).__init__(data)

        # TapeLibrary's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # TapeLibrary's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        self.managementip = None
        # Rack units
        self.nb_u = None
        # TapeLibrary's serial number
        self.serialnumber = None
        # TapeLibrary's asset number
        self.asset_number = None
        # TapeLibrary's move to production date
        self.move2production = None
        # TapeLibrary's purchase date
        self.purchase_date = None
        # TapeLibrary's end of warranty date
        self.end_of_warranty = None
        # TapeLibrary's description, as a free text
        self.description = None

        ##############################
        #           Lists            #
        ##############################
        # TapeLibrary's softwares list
        self.softwares_list = {}
        # TapeLibrary's contacts list
        self.contacts_list = {}
        # TapeLibrary's documents list
        self.documents_list = {}
        # TapeLibrary's tickets list
        self.tickets_list = {}
        # TapeLibrary's application solutions list
        self.applicationsolution_list = {}
        # TapeLibrary's network interfaces list
        self.physicalinterface_list = {}
        # TapeLibrary's FC ports list
        self.fiberinterfacelist_list = {}
        # TapeLibrary's network devices list
        self.networkdevice_list = {}
        # TapeLibrary's SANs list
        self.san_list = {}
        # TapeLibrary's provider contracts list
        self.providercontracts_list = {}
        # TapeLibrary's services list
        self.services_list = {}
        # List of Tapes
        self.tapes_list = {}

# Register as a subclass of Datacenter Device
ItopapiDatacenterDevice.register(ItopapiTapeLibrary)