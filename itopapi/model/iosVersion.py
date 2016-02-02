# -*- coding: utf8 -*-fr

"""
ItopapiIOSVersion is an abstraction of IOSVersion representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.typology import ItopapiTypology
from itopapi.model.features.hasBrand import HasBrand

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiIOSVersion(ItopapiTypology, HasBrand):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'IOSVersion',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': [
            HasBrand.foreign_key,
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of IOSVersion with the given key or criteria """
        return ItopapiPrototype.find(ItopapiIOSVersion, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiIOSVersion, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of IOSVersion """
        return ItopapiPrototype.find_all(ItopapiIOSVersion)

    """
    ItopapiIOSVersion is an object that represents an IOSVersion from iTop
    """
    def __init__(self, data=None):
        super(ItopapiIOSVersion, self).__init__(data)


# Register as a subclass of Typology
ItopapiTypology.register(ItopapiIOSVersion)
