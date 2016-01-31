# -*- coding: utf8 -*-fr

"""
ItopapiBrand is an abstraction of Brand representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.typology import ItopapiTypology

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiBrand(ItopapiTypology):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Brand',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Brand with the given key or criteria """
        return ItopapiPrototype.find(ItopapiBrand, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiBrand, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Brand """
        return ItopapiPrototype.find_all(ItopapiBrand)

    """
    ItopapiBrand is an object that represents a Brand from iTop
    """
    def __init__(self, data=None):
        super(ItopapiBrand, self).__init__(data)

        # Physical devices using this brand
        self.physicaldevices_list = None


# Register as a subclass of Typology
ItopapiTypology.register(ItopapiBrand)
