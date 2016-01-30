# -*- coding: utf8 -*-fr

"""
ItopapiPowerSource is an abstraction of PowerSource representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation
from itopapi.model.features.hasBrand import HasBrand

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPowerSource(ItopapiPrototype, HasOrganization, HasLocation, HasBrand):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'PowerSource',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'serialnumber', 'asset_number',
                 'move2production', 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasLocation.foreign_key,
            HasBrand.foreign_key,
            {'id': 'model_id', 'name': 'model_name', 'table': 'Model'},
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PowerSource with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPowerSource, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPowerSource, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of PowerSource """
        return ItopapiPrototype.find_all(ItopapiPowerSource)

    """
    ItopapiPowerSource is an object that represents a PowerSource from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPowerSource, self).__init__(data)

        # PowerSource's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # PowerSource's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        self.model_id = None
        self.model_id_friendlyname = None
        self.model_name = None
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

    def find_model(self):
        """
        Retrieve the ItopapiModel corresponding to this instance
        """
        if self.model_id is not None:
            return ItopapiPrototype.get_itop_class('Model').find(self.model_id)
        return None
