# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasConnectableCI is a mixin representing the ConnectableCI attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasConnectableCI(object):
    """
    HasConnectableCI represents the ConnectableCI attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'connectableci_id', 'name': 'connectableci_name', 'table': 'Person'}

    def __init__(self):
        super(HasConnectableCI, self).__init__()

        # Object's connectableci id. Call find_connectableci to get the full information or just use connectableci_name
        self.connectableci_id = None
        # Object's connectableci id's friendly name. Not sure the difference with connectableci_name
        self.connectableci_id_friendlyname = None
        # Object's connectableci name
        self.connectableci_name = None

    def find_connectableci(self):
        """
        Retrieve the ItopapiConnectableCI related to this instance
        """
        if self.connectableci_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.connectableci_id)
        return None

    def set_connectableci(self, connectableci):
        """
        Set the ItopapiPerson parameters
        """
        self.connectableci_id = connectableci.instance_id
        self.connectableci_id_friendlyname = connectableci.friendlyname
        self.connectableci_name = connectableci.name
