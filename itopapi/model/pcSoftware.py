# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
ItopapiPCSoftware is an abstraction of PCSoftware representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.softwareInstance import ItopapiSoftwareInstance
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasSoftwareLicence import HasSoftwareLicence
from itopapi.model.features.hasSoftware import HasSoftware

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiPCSoftware(ItopapiSoftwareInstance, HasOrganization, HasSoftwareLicence, HasSoftware):
    """
    ItopapiPCSoftware is an object that represents a PCSoftware from iTop
    """

    """ Configuration specific to itop """
    itop = {
        # Name of the class in Itop
        'name': 'PCSoftware',
        # Define which fields to save when creating or updating from the python API
        'save': ['move2production', 'description', 'status', 'name', 'business_criticity', 'path'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasSoftware.foreign_key,
            HasSoftwareLicence.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PCSoftware with the given key or criteria """
        return ItopapiPrototype.find(ItopapiPCSoftware, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiPCSoftware, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Rack """
        return ItopapiPrototype.find_all(ItopapiPCSoftware)

    def __init__(self, data=None):
        super(ItopapiPCSoftware, self).__init__(data)

        ##################################
        #           Properties           #
        ##################################
        # PCSoftware's status. Values within [implementation, obsolete, production, stock]
        self.status = None
        # PCSoftware's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # PCSoftware's path ?
        self.path = None
        # PCSoftware's description, as a free text
        self.description = None
        # PCSoftware's move to production date
        self.move2production = None

        ##################################
        #             Lists              #
        ##################################
        self.documents_list = {}
        self.softwares_list = {}
        self.tickets_list = {}
        self.services_list = {}
        self.contacts_list = {}
        self.providercontracts_list = {}
        self.applicationsolution_list = {}


# Register as a subclass of SoftwareInstance
ItopapiSoftwareInstance.register(ItopapiPCSoftware)

