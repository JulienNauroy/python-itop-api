# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiOrganization is an abstraction of Organization representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.deliveryModel import ItopapiDeliveryModel
from itopapi.model.features.hasParentOrganization import HasParentOrganization
from itopapi.model.features.hasDeliveryModel import HasDeliveryModel

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiOrganization(ItopapiPrototype, HasParentOrganization, HasDeliveryModel):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Organization',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'code', 'status'],
        'foreign_keys': [
            HasParentOrganization.foreign_key,
            HasDeliveryModel.foreign_key,
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiOrganization, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiOrganization, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiOrganization)

    """
    ItopapiOrganization is an object that represents an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiOrganization, self).__init__(data)

        self.code = None
        # Application Solution's status. Values within [inactive, active]
        self.status = None
