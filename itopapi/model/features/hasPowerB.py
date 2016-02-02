# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasPowerB is a mixin representing the powerB attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasPowerB(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'powerB_id', 'name': 'powerB_name', 'table': 'Power'}

    def __init__(self):
        super(HasPowerB, self).__init__()

        # Object's powerB id. Call find_powerB to get the full information or just use powerB_name
        self.powerB_id = None
        # Object's powerB id's friendly name. Not sure the difference with powerB_name
        self.powerB_id_friendlyname = None
        # Object's powerB name
        self.powerB_name = None

    def find_powerB(self):
        """
        Retrieve the ItopapiAgent related to this instance
        """
        if self.powerB_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.powerB_id)
        return None

    def set_powerB(self, powerB):
        """
        Set the ItopapiPerson parameters
        """
        self.powerB_id = powerB.instance_id
        self.powerB_id_friendlyname = powerB.friendlyname
        self.powerB_name = powerB.name
