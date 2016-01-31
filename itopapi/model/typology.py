# -*- coding: utf8 -*-fr

"""
ItopapiTypology is an abstraction of Typology representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiTypology(ItopapiPrototype):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'Typology',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Functional CI with the given key or criteria """
        return ItopapiPrototype.find(ItopapiTypology, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiTypology, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Functional CI """
        return ItopapiPrototype.find_all(ItopapiTypology)

    """
    ItopapiTypology is an object that represents a Functional CI from iTop
    """
    def __init__(self, data=None):
        super(ItopapiTypology, self).__init__(data)
