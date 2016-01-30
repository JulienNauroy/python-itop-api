# -*- coding: utf8 -*-fr

"""
ItopapiIncident is a abstraction of a Incident representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype
from itopapi.model.features.hasOrganization import HasOrganization

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiIncident(ItopapiPrototype, HasOrganization):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Incident',
        # Define which fields to save when creating or updating from the python API
        'save': ['title', 'description', 'ref', 'start_date', 'end_date', 'close_date', 'last_update'],
        'foreign_keys': [
            HasOrganization.foreign_key,
            {'id': 'agent_id', 'name': 'agent_name', 'table': 'Person'},
            {'id': 'team_id', 'name': 'team_name', 'table': 'Team'},
        ],
        'list_types': {
            'functionalcis_list': 'functionalci_id_finalclass_recall',
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of PhysicalInterface with the given key or criteria """
        return ItopapiPrototype.find(ItopapiIncident, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiIncident, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Person """
        return ItopapiPrototype.find_all(ItopapiIncident)

    """
    ItopapiPerson is an object that represents a Person from iTop
    """
    def __init__(self, data=None):
        super(ItopapiIncident, self).__init__(data)
        self.title = None
        self.friendlyname = None
        self.description = None
        self.ref = None
        self.start_date = None
        self.end_date = None
        self.close_date = None
        self.last_update = None

        # Foreign key to a Person
        self.agent_id = None
        self.agent_name = None

        self.team_id = None
        self.team_id_friendlyname = None
        self.team_name = None

        ##################################
        #             Lists              #
        ##################################
        self.functionalcis_list = None
        self.contacts_list = None
        self.workers_list = None
        self.private_log = None
