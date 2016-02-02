# -*- coding: utf8 -*-fr

"""
ItopapiDocumentType is an abstraction of DocumentType representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.typology import ItopapiTypology

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiDocumentType(ItopapiTypology):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'DocumentType',
        # Define which fields to save when creating or updating from the python API
        'save': ['name'],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of DocumentType with the given key or criteria """
        return ItopapiPrototype.find(ItopapiDocumentType, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiDocumentType, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of DocumentType """
        return ItopapiPrototype.find_all(ItopapiDocumentType)

    """
    ItopapiDocumentType is an object that represents an DocumentType from iTop
    """
    def __init__(self, data=None):
        super(ItopapiDocumentType, self).__init__(data)


# Register as a subclass of Typology
ItopapiTypology.register(ItopapiDocumentType)
