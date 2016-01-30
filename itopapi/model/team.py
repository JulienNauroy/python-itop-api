# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
ItopapiTeam is an abstraction of Team representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiTeam(ItopapiPrototype, HasOrganization):
    """
    ItopapiTeam is an object that represents a Team from iTop
    """

    """ Configuration specific to itop """
    itop = {
        # Name of the class in Itop
        'name': 'Team',
        # Define which fields to save when creating or updating from the python API
        'save': ['status', 'phone', 'notify', 'name', 'function', 'email'],
        'foreign_keys': [
            HasOrganization.foreign_key,
        ],
        'list_types': {
            'persons_list': 'Person',
            'cis_list': 'functionalci_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Team with the given key or criteria """
        return ItopapiPrototype.find(ItopapiTeam, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiTeam, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Rack """
        return ItopapiPrototype.find_all(ItopapiTeam)

    def __init__(self, data=None):
        super(ItopapiTeam, self).__init__(data)

        ##################################
        #           Properties           #
        ##################################
        self.status = None
        self.phone = None
        self.notify = None
        self.function = None
        self.email = None
        ##################################
        #             Lists              #
        ##################################
        self.cis_list = None
        self.tickets_list = None
        self.persons_list = None
