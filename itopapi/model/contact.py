# -*- coding: utf8 -*-fr

"""
ItopapiContact is an abstraction of Contact representation on iTop
It serves as a base class for Person and Team
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiContact(ItopapiPrototype):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'Contact',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Contact with the given key or criteria """
        return ItopapiPrototype.find(ItopapiContact, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiContact, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Contact """
        return ItopapiPrototype.find_all(ItopapiContact)

    """
    ItopapiContact is an object that represents a Contact from iTop
    """
    def __init__(self, data=None):
        super(ItopapiContact, self).__init__(data)
