# -*- coding: utf8 -*-fr

"""
ItopapiPDU is an abstraction of PDU representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.powerConnection import ItopapiPowerConnection
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation
from itopapi.model.features.hasBrand import HasBrand
from itopapi.model.features.hasModel import HasModel
from itopapi.model.features.hasRack import HasRack
from itopapi.model.features.hasPowerStart import HasPowerStart

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPDU(ItopapiPowerConnection, HasOrganization, HasLocation, HasBrand, HasModel, HasRack, HasPowerStart):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'PDU',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'serialnumber', 'asset_number',
                 'move2production', 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasLocation.foreign_key,
            HasBrand.foreign_key,
            HasModel.foreign_key,
            HasPowerStart.foreign_key,
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PDU with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPDU, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPDU, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PDU """
        return ItopapiPrototype.find_all(ItopapiPDU)

    """
    ItopapiPDU is an object that represents a PDU from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPDU, self).__init__(data)

        # PDU's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # PDU's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Serial number
        self.serialnumber = None
        # Asset number
        self.asset_number = None
        # Server's move to production date
        self.move2production = None
        # Server's purchase date
        self.purchase_date = None
        # Server's end of warranty date
        self.end_of_warranty = None
        self.description = None
        ##################################
        #             Lists              #
        ##################################
        self.documents_list = {}
        self.softwares_list = {}
        self.services_list = {}
        self.applicationsolution_list = {}
        self.contacts_list = {}
        self.tickets_list = {}
        self.providercontracts_list = {}
        self.pdus_list = {}
