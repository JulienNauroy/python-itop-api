# -*- coding: utf8 -*-fr

"""
ItopapiPatch is an abstraction of Patch representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPatch(ItopapiPrototype):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'Patch',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Patch with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPatch, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPatch, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Patch """
        return ItopapiPrototype.find_all(ItopapiPatch)

    """
    ItopapiPatch is an object that represents a Patch from iTop
    """
    def __init__(self, data=None):
        super(ItopapiPatch, self).__init__(data)
