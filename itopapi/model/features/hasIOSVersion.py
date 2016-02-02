# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasIOSVersion is a mixin representing the iosversion attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasIOSVersion(object):
    """
    HasIOSVersion represents the IOSVersion attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'iosversion_id', 'name': 'iosversion_name', 'table': 'IOSVersion'}

    def __init__(self):
        super(HasIOSVersion, self).__init__()

        # Object's iosversion id. Call find_iosversion to get the full information or just use iosversion_name
        self.iosversion_id = None
        # Object's iosversion id's friendly name. Not sure the difference with iosversion_name
        self.iosversion_id_friendlyname = None
        # Object's iosversion name
        self.iosversion_name = None

    def find_iosversion(self):
        """
        Retrieve the ItopapiIOSVersion related to this instance
        """
        if self.iosversion_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.iosversion_id)
        return None

    def set_iosversion(self, iosversion):
        """
        Set the ItopapiPerson parameters
        """
        self.iosversion_id = iosversion.instance_id
        self.iosversion_id_friendlyname = iosversion.friendlyname
        self.iosversion_name = iosversion.name
