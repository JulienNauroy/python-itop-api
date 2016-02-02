# -*- coding: utf8 -*-fr

"""
ItopapiContractType is an abstraction of ContractType representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.typology import ItopapiTypology

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiContractType(ItopapiTypology):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'ContractType',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of ContractType with the given key or criteria """
        return ItopapiPrototype.find(ItopapiContractType, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiContractType, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of ContractType """
        return ItopapiPrototype.find_all(ItopapiContractType)

    """
    ItopapiContractType is an object that represents an ContractType from iTop
    """
    def __init__(self, data=None):
        super(ItopapiContractType, self).__init__(data)


# Register as a subclass of Typology
ItopapiTypology.register(ItopapiContractType)
