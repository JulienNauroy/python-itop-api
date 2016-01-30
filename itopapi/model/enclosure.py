# -*- coding: utf8 -*-fr

"""
ItopapiEnclosure is an abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiEnclosure(ItopapiPrototype, HasOrganization, HasLocation):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Enclosure',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'nb_u', 'serialnumber', 'asset_number',
                 'move2production', 'purchase_date', 'end_of_warranty', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasLocation.foreign_key,
            {'id': 'rack_id', 'name': 'rack_name', 'table': 'Rack'},
            {'id': 'brand_id', 'name': 'brand_name', 'table': 'Brand'},
            {'id': 'model_id', 'name': 'model_name', 'table': 'Model'},
        ],
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Enclosure with the given key or criteria """
        return ItopapiPrototype.find(ItopapiEnclosure, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiEnclosure, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Enclosure """
        return ItopapiPrototype.find_all(ItopapiEnclosure)

    """
    ItopapiEnclosure is an object that represents an Enclosure from iTop
    """
    def __init__(self, data=None):
        super(ItopapiEnclosure, self).__init__(data)
        # Enclosure's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # Enclosure's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Enclosure's rack id. Call findRack to get the full information or just use rack_id
        # friendlyname and rack_name
        self.rack_id = None
        # Enclosure's rack id's friendly name. Not sure the difference with rack_name
        self.rack_id_friendlyname = None
        # Enclosure's rack name
        self.rack_name = None
        self.brand_id = None
        self.brand_id_friendlyname = None
        self.brand_name = None
        self.model_id = None
        self.model_id_friendlyname = None
        self.model_name = None
        # Rack units
        self.nb_u = None
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

    def find_rack(self):
        """
        Retrieve the ItopapiRack corresponding to this server
        """
        if self.rack_id is not None:
            return ItopapiPrototype.get_itop_class('Rack').find(self.rack_id)
        return None

    def find_brand(self):
        """
        Retrieve the ItopapiBrand corresponding to this instance
        """
        if self.brand_id is not None:
            return ItopapiPrototype.get_itop_class('Brand').find(self.brand_id)
        return None

    def find_model(self):
        """
        Retrieve the ItopapiModel corresponding to this instance
        """
        if self.model_id is not None:
            return ItopapiPrototype.get_itop_class('Model').find(self.model_id)
        return None
