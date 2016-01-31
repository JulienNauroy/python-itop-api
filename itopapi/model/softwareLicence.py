# -*- coding: utf8 -*-fr

"""
ItopapiSoftwareLicence is an abstraction of Rack representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.licence import ItopapiLicence
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasSoftware import HasSoftware

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiSoftwareLicence(ItopapiLicence, HasOrganization, HasSoftware):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'SoftwareLicence',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'usage_limit', 'description', 'perpetual', 'start_date', 'end_date', 'licence_key'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasSoftware.foreign_key,
        ],
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of SoftwareLicence with the given key or criteria """
        return ItopapiPrototype.find(ItopapiSoftwareLicence, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiSoftwareLicence, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of SoftwareLicence """
        return ItopapiPrototype.find_all(ItopapiSoftwareLicence)

    """
    ItopapiSoftwareLicence is an object that represents an SoftwareLicence (sic) from iTop
    """
    def __init__(self, data=None):
        super(ItopapiSoftwareLicence, self).__init__(data)
        # Number of concurrent users or licences
        self.usage_limit = None
        self.description = None
        # Possible values are ['yes', 'no']
        self.perpetual = 'no'
        self.start_date = None
        self.end_date = None
        self.licence_key = None
        # Lists
        self.documents_list = []
        self.softwareinstance_list = []


# Register as a subclass of FunctionalCI
ItopapiLicence.register(ItopapiSoftwareLicence)
