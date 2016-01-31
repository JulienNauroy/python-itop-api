# -*- coding: utf8 -*-fr

"""
ItopapiOSVersion is an abstraction of an OSVersion representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.typology import ItopapiTypology
from itopapi.model.features.hasOSFamily import HasOSFamily

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiOSVersion(ItopapiTypology, HasOSFamily):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'OSVersion',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': [
            HasOSFamily.foreign_key,
        ]
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of OSVersion with the given key or criteria """
        return ItopapiPrototype.find(ItopapiOSVersion, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiOSVersion, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSVersion """
        return ItopapiPrototype.find_all(ItopapiOSVersion)

    """
    ItopapiOSVersion is an object that represents an OS Version from iTop
    """
    def __init__(self, data=None):
        super(ItopapiOSVersion, self).__init__(data)


# Register as a subclass of Typology
ItopapiTypology.register(ItopapiOSVersion)
