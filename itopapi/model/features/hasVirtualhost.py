# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasVirtualHost is a mixin representing the virtualhost attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasVirtualHost(object):
    """
    HasVirtualHost represents the VirtualHost attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'virtualhost_id', 'name': 'virtualhost_name', 'table': 'VirtualHost'}

    def __init__(self):
        super(HasVirtualHost, self).__init__()

        # Object's virtualhost id. Call find_virtualhost to get the full information or just use
        # virtualhost_id_friendlyname and virtualhost_name
        self.virtualhost_id = None
        # Object's virtualhost id's friendly name. Not sure the difference with virtualhost_name
        self.virtualhost_id_friendlyname = None
        # Object's virtualhost name
        self.virtualhost_name = None

    def find_virtualhost(self):
        """
        Retrieve the ItopapiVirtualHost related to this instance
        """
        if self.virtualhost_id is not None:
            return ItopapiPrototype.get_itop_class('VirtualHost').find(self.virtualhost_id)
        return None

    def set_virtualhost(self, virtualhost):
        """
        Set the ItopapiVirtualHost parameters
        """
        self.virtualhost_id = virtualhost.instance_id
        self.virtualhost_id_friendlyname = virtualhost.friendlyname
        self.virtualhost_name = virtualhost.name
