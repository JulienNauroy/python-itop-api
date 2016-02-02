# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasPowerA is a mixin representing the powerA attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasPowerA(object):
    """
    HasPowerA represents the Power attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'powerA_id', 'name': 'powerA_name', 'table': 'Power'}

    def __init__(self):
        super(HasPowerA, self).__init__()

        # Object's powerA id. Call find_powerA to get the full information or just use powerA_name
        self.powerA_id = None
        # Object's powerA id's friendly name. Not sure the difference with powerA_name
        self.powerA_id_friendlyname = None
        # Object's powerA name
        self.powerA_name = None

    def find_powerA(self):
        """
        Retrieve the ItopapiAgent related to this instance
        """
        if self.powerA_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.powerA_id)
        return None

    def set_powerA(self, powerA):
        """
        Set the ItopapiPerson parameters
        """
        self.powerA_id = powerA.instance_id
        self.powerA_id_friendlyname = powerA.friendlyname
        self.powerA_name = powerA.name
