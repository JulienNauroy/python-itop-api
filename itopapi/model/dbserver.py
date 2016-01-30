# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
ItopapiDBServer is a abstraction of DBServer representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.othersoftware import ItopapiOtherSoftware

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiDBServer(ItopapiOtherSoftware):
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
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
            {'id': 'software_id', 'name': 'software_name', 'table': 'Software'},
            {'id': 'softwarelicence_id', 'name': 'softwarelicence_name', 'table': 'SoftwareLicence'},
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
