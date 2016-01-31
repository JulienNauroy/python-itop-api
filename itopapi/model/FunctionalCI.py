# -*- coding: utf8 -*-fr

"""
ItopapiFunctionalCI is an abstraction of Functional CI representation on iTop
It serves as a base class for a lot of subclasses.
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiFunctionalCI(ItopapiPrototype):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'FunctionalCI',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Functional CI with the given key or criteria """
        return ItopapiPrototype.find(ItopapiFunctionalCI, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiFunctionalCI, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Functional CI """
        return ItopapiPrototype.find_all(ItopapiFunctionalCI)

    """
    ItopapiFunctionalCI is an object that represents a Functional CI from iTop
    """
    def __init__(self, data=None):
        super(ItopapiFunctionalCI, self).__init__(data)
