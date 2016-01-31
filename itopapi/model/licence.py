# -*- coding: utf8 -*-fr

"""
ItopapiLicence is an abstraction of Licence representation on iTop
"""

from abc import ABCMeta
from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiLicence(ItopapiPrototype):
    __metaclass__ = ABCMeta

    # Configuration specific to itop
    itop = {
        'name': 'Licence',
        'save': [],
        'foreign_keys': []
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Licence with the given key or criteria """
        return ItopapiPrototype.find(ItopapiLicence, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiLicence, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Licence """
        return ItopapiPrototype.find_all(ItopapiLicence)

    """
    ItopapiLicence is an object that represents a Licence from iTop
    """
    def __init__(self, data=None):
        super(ItopapiLicence, self).__init__(data)
