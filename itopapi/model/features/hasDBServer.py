# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasDBServer is a mixin representing the dbserver attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasDBServer(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'dbserver_id', 'name': 'dbserver_name', 'table': 'DBServer'}

    def __init__(self):
        super(HasDBServer, self).__init__()

        # Object's dbserver id. Call find_dbserver to get the full information or just use
        # dbserver_id_friendlyname and dbserver_name
        self.dbserver_id = None
        # Object's dbserver id's friendly name. Not sure the difference with dbserver_name
        self.dbserver_id_friendlyname = None
        # Object's dbserver name
        self.dbserver_name = None

    def find_dbserver(self):
        """
        Retrieve the ItopapiDBServer related to this instance
        """
        if self.dbserver_id is not None:
            return ItopapiPrototype.get_itop_class('DBServer').find(self.dbserver_id)
        return None

    def set_dbserver(self, dbserver):
        """
        Set the ItopapiDBServer parameters
        """
        self.dbserver_id = dbserver.instance_id
        self.dbserver_id_friendlyname = dbserver.friendlyname
        self.dbserver_name = dbserver.name
