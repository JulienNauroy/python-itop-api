# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasWebServer is a mixin representing the webserver attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasWebServer(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'webserver_id', 'name': 'webserver_name', 'table': 'WebServer'}

    def __init__(self):
        super(HasWebServer, self).__init__()

        # Object's webserver id. Call find_webserver to get the full information or just use
        # webserver_id_friendlyname and webserver_name
        self.webserver_id = None
        # Object's webserver id's friendly name. Not sure the difference with webserver_name
        self.webserver_id_friendlyname = None
        # Object's webserver name
        self.webserver_name = None

    def find_webserver(self):
        """
        Retrieve the ItopapiWebServer related to this instance
        """
        if self.webserver_id is not None:
            return ItopapiPrototype.get_itop_class('WebServer').find(self.webserver_id)
        return None

    def set_webserver(self, webserver):
        """
        Set the ItopapiWebServer parameters
        """
        self.webserver_id = webserver.instance_id
        self.webserver_id_friendlyname = webserver.friendlyname
        self.webserver_name = webserver.name
