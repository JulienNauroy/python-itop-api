# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
ItopapiDBServer is an abstraction of DBServer representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.softwareInstance import ItopapiSoftwareInstance
from itopapi.model.features.hasOrganization import HasOrganization
from itopapi.model.features.hasSoftware import HasSoftware
from itopapi.model.features.hasSoftwareLicence import HasSoftwareLicence
from itopapi.model.features.hasSystem import HasSystem

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiDBServer(ItopapiSoftwareInstance, HasOrganization, HasSoftware, HasSoftwareLicence, HasSystem):
    """
    ItopapiDBServer is an object that represents a DBServer from iTop
    It has the same attributes as ItopapiOtherSoftware
    """

    """ Configuration specific to itop """
    itop = {
        # Name of the class in Itop
        'name': 'DBServer',
        # Define which fields to save when creating or updating from the python API
        'save': ['move2production', 'description', 'status', 'name', 'business_criticity', 'path'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            HasSoftware.foreign_key,
            HasSoftwareLicence.foreign_key,
            HasSystem.foreign_key,
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of DBServer with the given key or criteria """
        return ItopapiPrototype.find(ItopapiDBServer, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiDBServer, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Rack """
        return ItopapiPrototype.find_all(ItopapiDBServer)

    def __init__(self, data=None):
        super(ItopapiDBServer, self).__init__(data)


# Register as a subclass of SoftwareInstance
ItopapiSoftwareInstance.register(ItopapiDBServer)
