# -*- coding: utf8 -*-fr

"""
ItopapiOSLicence is an abstraction of OSLicence representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.licence import ItopapiLicence
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasOSVersion import HasOSVersion

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiOSLicence(ItopapiLicence, HasOrganization, HasOSVersion):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'OSLicence',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'usage_limit', 'description', 'perpetual', 'start_date', 'end_date', 'licence_key'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasOSVersion.foreign_key,
        ],
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of OSLicence with the given key or criteria """
        return ItopapiPrototype.find(ItopapiOSLicence, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiOSLicence, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of OSLicence """
        return ItopapiPrototype.find_all(ItopapiOSLicence)

    """
    ItopapiOSLicence is an object that represents an OSLicence (sic) from iTop
    """
    def __init__(self, data=None):
        super(ItopapiOSLicence, self).__init__(data)
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
        self.servers_list = []
        self.virtualmachines_list = []


# Register as a subclass of FunctionalCI
ItopapiLicence.register(ItopapiOSLicence)
