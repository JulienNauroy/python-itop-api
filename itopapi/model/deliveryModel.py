# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
ItopapiDeliveryModel is an abstraction of Organization representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']

class ItopapiDeliveryModel(ItopapiPrototype, HasOrganization):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'DeliveryModel',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'description'],
        'foreign_keys': [
            HasOrganization.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ApplicationSolution with the given key or criteria """
        return ItopapiPrototype.find(ItopapiDeliveryModel, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiDeliveryModel, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSFamily """
        return ItopapiPrototype.find_all(ItopapiDeliveryModel)

    """
    ItopapiDeliveryModel is an object that represents an Application Solution from iTop
    """
    def __init__(self, data=None):
        super(ItopapiDeliveryModel, self).__init__(data)

        self.description = None

        ##################################
        #              Lists             #
        ##################################
        self.customers_list = []
        self.contacts_list = []
