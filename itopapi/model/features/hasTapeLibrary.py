# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasTapeLibrary is a mixin representing the tapelibrary attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasTapeLibrary(object):
    """
    HasTapeLibrary represents the TapeLibrary attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'tapelibrary_id', 'name': 'tapelibrary_name', 'table': 'TapeLibrary'}

    def __init__(self):
        super(HasTapeLibrary, self).__init__()

        # Object's tapelibrary id. Call find_tapelibrary to get the full information or just use tapelibrary_name
        self.tapelibrary_id = None
        # Object's tapelibrary id's friendly name. Not sure the difference with tapelibrary_name
        self.tapelibrary_id_friendlyname = None
        # Object's tapelibrary name
        self.tapelibrary_name = None

    def find_tapelibrary(self):
        """
        Retrieve the ItopapiTapeLibrary related to this instance
        """
        if self.tapelibrary_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.tapelibrary_id)
        return None

    def set_tapelibrary(self, tapelibrary):
        """
        Set the ItopapiPerson parameters
        """
        self.tapelibrary_id = tapelibrary.instance_id
        self.tapelibrary_id_friendlyname = tapelibrary.friendlyname
        self.tapelibrary_name = tapelibrary.name
