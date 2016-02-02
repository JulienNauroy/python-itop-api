# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasEnclosure is a mixin representing the enclosure attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasEnclosure(object):
    """
    HasEnclosure represents the Enclosure attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'enclosure_id', 'name': 'enclosure_name', 'table': 'Enclosure'}

    def __init__(self):
        super(HasEnclosure, self).__init__()

        # Object's enclosure id. Call find_enclosure to get the full information or just use
        # enclosure_id_friendlyname and enclosure_name
        self.enclosure_id = None
        # Object's enclosure id's friendly name. Not sure the difference with enclosure_name
        self.enclosure_id_friendlyname = None
        # Object's enclosure name
        self.enclosure_name = None

    def find_enclosure(self):
        """
        Retrieve the ItopapiEnclosure related to this instance
        """
        if self.enclosure_id is not None:
            return ItopapiPrototype.get_itop_class('Enclosure').find(self.enclosure_id)
        return None

    def set_enclosure(self, enclosure):
        """
        Set the ItopapiEnclosure parameters
        """
        self.enclosure_id = enclosure.instance_id
        self.enclosure_id_friendlyname = enclosure.friendlyname
        self.enclosure_name = enclosure.name
