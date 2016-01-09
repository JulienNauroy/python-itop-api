# -*- coding: utf8 -*-fr

"""
ItopapiPowerSource is a abstraction of PowerSource representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPowerSource(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'PowerSource',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'serialnumber', 'asset_number',
                 'move2production', 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'location_id', 'name': 'location_name', 'table': 'Location'},
            {'id': 'brand_id', 'name': 'brand_name', 'table': 'Brand'},
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

        # PowerSource's organization id. Call find_organization to get the full information or just
        #  use org_id_friendlyname and organization_name
        self.org_id = None
        # PowerSource's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # PowerSource's organization name
        self.organization_name = None
        # PowerSource's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # PowerSource's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # PowerSource's location id. Call find_location to get the full information or just use
        # location_id_friendlyname and location_name
        self.location_id = None
        # PowerSource's location id's friendly name. Not sure the difference with location_name
        self.location_id_friendlyname = None
        # PowerSource's location name
        self.location_name = None
        self.brand_id = None
        self.brand_id_friendlyname = None
        self.brand_name = None
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

    def find_organization(self):
        """
        Retrieve the ItopapiOrganization corresponding to this server
        """
        if self.org_id is not None:
            ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None

    def find_location(self):
        """
        Retrieve the ItopapiLocation related to this instance
        """
        if self.location_id is not None:
            ItopapiPrototype.get_itop_class('Location').find(self.location_id)
        return None

    def find_brand(self):
        """
        Retrieve the ItopapiBrand corresponding to this instance
        """
        if self.brand_id is not None:
            ItopapiPrototype.get_itop_class('Brand').find(self.brand_id)
        return None

    def find_model(self):
        """
        Retrieve the ItopapiModel corresponding to this instance
        """
        if self.model_id is not None:
            ItopapiPrototype.get_itop_class('Model').find(self.model_id)
        return None
