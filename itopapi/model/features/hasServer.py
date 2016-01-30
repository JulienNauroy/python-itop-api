# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasServer is a mixin representing the server attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasServer(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'server_id', 'name': 'server_name', 'table': 'Server'}

    def __init__(self):
        super(HasServer, self).__init__()

        # Object's server id. Call find_server to get the full information or just use
        # server_id_friendlyname and server_name
        self.server_id = None
        # Object's server id's friendly name. Not sure the difference with server_name
        self.server_id_friendlyname = None
        # Object's server name
        self.server_name = None

    def find_server(self):
        """
        Retrieve the ItopapiServer related to this instance
        """
        if self.server_id is not None:
            return ItopapiPrototype.get_itop_class('Server').find(self.server_id)
        return None

    def set_server(self, server):
        """
        Set the ItopapiServer parameters
        """
        self.server_id = server.instance_id
        self.server_id_friendlyname = server.friendlyname
        self.server_name = server.name
