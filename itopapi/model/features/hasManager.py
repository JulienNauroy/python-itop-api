# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasManager is a mixin representing the manager attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasManager(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'manager_id', 'name': 'manager_name', 'table': 'Person'}

    def __init__(self):
        super(HasManager, self).__init__()

        # Object's manager id. Call find_manager to get the full information or just use manager_name
        self.manager_id = None
        # Object's manager name
        self.manager_name = None

    def find_manager(self):
        """
        Retrieve the ItopapiManager related to this instance
        """
        if self.manager_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.manager_id)
        return None

    def set_manager(self, manager):
        """
        Set the ItopapiPerson parameters
        """
        self.manager_id = manager.instance_id
        self.manager_name = manager.name
