# -*- coding: utf8 -*-fr

"""
ItopapiEnclosure is an abstraction of Enclosure representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasLocation import HasLocation
from itopapi.model.features.hasBrand import HasBrand
from itopapi.model.features.hasModel import HasModel
from itopapi.model.features.hasRack import HasRack

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiEnclosure(ItopapiPrototype, HasOrganization, HasLocation, HasBrand, HasModel, HasRack):

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
            HasBrand.foreign_key,
            HasModel.foreign_key,
            HasRack.foreign_key,
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
