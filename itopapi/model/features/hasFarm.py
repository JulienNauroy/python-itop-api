# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasFarm is a mixin representing the farm attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasFarm(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'farm_id', 'name': 'farm_name', 'table': 'Farm'}

    def __init__(self):
        super(HasFarm, self).__init__()

        # Object's farm id. Call find_farm to get the full information or just use
        # farm_id_friendlyname and farm_name
        self.farm_id = None
        # Object's farm id's friendly name. Not sure the difference with farm_name
        self.farm_id_friendlyname = None
        # Object's farm name
        self.farm_name = None

    def find_farm(self):
        """
        Retrieve the ItopapiFarm related to this instance
        """
        if self.farm_id is not None:
            return ItopapiPrototype.get_itop_class('Farm').find(self.farm_id)
        return None

    def set_farm(self, farm):
        """
        Set the ItopapiOrganization parameters
        """
        self.farm_id = farm.instance_id
        self.farm_id_friendlyname = farm.friendlyname
        self.farm_name = farm.name
