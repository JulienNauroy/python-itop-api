# -*- coding: utf8 -*-fr

"""
ItopapiFarm is a abstraction of a virtual servers farm representation on iTop
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class ItopapiFarm(ItopapiPrototype):

    # Configuration specific to itop
    itop = {
        # Name of the class in Itop
        'name': 'Farm',
        # Define which fields to save when creating or updating from the python API
        'save': ['name', 'status', 'business_criticity', 'move2production', 'description'],
        'foreign_keys': [
            {'id': 'org_id', 'name': 'organization_name', 'table': 'Organization'},
        ],
        'list_types': {
            'contacts_list': 'contact_id_finalclass_recall'
        },
    }

    @staticmethod
    def find(key):
        """ Retrieve one or more instance of Farm with the given key or criteria """
        return ItopapiPrototype.find(ItopapiFarm, key)

    @staticmethod
    def find_by_name(name):
        return ItopapiPrototype.find_by_name(ItopapiFarm, name)

    @staticmethod
    def find_all():
        """ Retrieve all instance of Farm """
        return ItopapiPrototype.find_all(ItopapiFarm)

    """
    ItopapiFarm is an object that represents a Farm from iTop
    """
    def __init__(self, data=None):
        super(ItopapiFarm, self).__init__(data)
        # Farm's organization id. Call find_organization to get the full information or just use
        #  org_id_friendlyname and organization_name
        self.org_id = None
        # Farm's organization friendly name. Not sure the difference with organization_name
        self.org_id_friendlyname = None
        # Farm's organization name
        self.organization_name = None
        # Farm's status. Values within [inactive, active]
        self.status = None
        # Farm's business criticity. Values within [high, medium, low]
        self.business_criticity = None
        # Farm's move to production date
        self.move2production = None
        # Farm's description, as a free text
        self.description = None
        ##################################
        #             Lists              #
        ##################################
        self.documents_list = None
        self.softwares_list = None
        self.applicationsolution_list = None
        self.tickets_list = None
        self.services_list = None
        self.logicalvolumes_list = None
        self.hypervisor_list = None
        self.virtualmachine_list = None


    def find_organization(self):
        """
        Retrieve the parent ItopapiOrganization
        """
        if self.org_id is not None:
            return ItopapiPrototype.get_itop_class('Organization').find(self.org_id)
        return None