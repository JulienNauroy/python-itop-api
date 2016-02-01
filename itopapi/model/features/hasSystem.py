# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasSystem is a mixin representing the FunctionalCI attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasSystem(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'system_id', 'name': 'system_name', 'table': 'FunctionalCI'}

    def __init__(self):
        super(HasSystem, self).__init__()

        # Object's system id. Call find_system to get the full information or just use system_name
        self.system_id = None
        # Object's system id's friendly name. Not sure the difference with system_name
        self.system_id_friendlyname = None
        # Object's system name
        self.system_name = None

    def find_system(self):
        """
        Retrieve the Itopapisystem related to this instance
        """
        if self.system_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.system_id)
        return None

    def set_system(self, system):
        """
        Set the ItopapiPerson parameters
        """
        self.system_id = system.instance_id
        self.system_id_friendlyname = system.friendlyname
        self.system_name = system.name
