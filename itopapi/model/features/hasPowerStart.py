# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasPowerStart is a mixin representing the powerstart attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasPowerStart(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'powerstart_id', 'name': 'powerstart_name', 'table': 'PowerConnection'}

    def __init__(self):
        super(HasPowerStart, self).__init__()

        # Object's powerstart id. Call find_powerstart to get the full information or just use powerstart_name
        self.powerstart_id = None
        # Object's powerstart id's friendly name. Not sure the difference with powerstart_name
        self.powerstart_id_friendlyname = None
        # Object's powerstart name
        self.powerstart_name = None

    def find_powerstart(self):
        """
        Retrieve the ItopapiPowerStart related to this instance
        """
        if self.powerstart_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.powerstart_id)
        return None

    def set_powerstart(self, powerstart):
        """
        Set the ItopapiPerson parameters
        """
        self.powerstart_id = powerstart.instance_id
        self.powerstart_id_friendlyname = powerstart.friendlyname
        self.powerstart_name = powerstart.name
