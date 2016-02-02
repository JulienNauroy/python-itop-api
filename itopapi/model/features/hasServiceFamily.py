# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasServiceFamily is a mixin representing the ServiceFamily attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasServiceFamily(object):
    """
    HasServiceFamily represents the ServiceFamily attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'servicefamily_id', 'name': 'servicefamily_name', 'table': 'ServiceFamily'}

    def __init__(self):
        super(HasServiceFamily, self).__init__()

        # Object's ServiceFamily id. Call find_servicefamily to get the full information or just use
        # servicefamily_id_friendlyname and servicefamily_name
        self.servicefamily_id = None
        # Object's ServiceFamily id's friendly name. Not sure the difference with servicefamily_name
        self.servicefamily_id_friendlyname = None
        # Object's ServiceFamily name
        self.servicefamily_name = None

    def find_servicefamily(self):
        """
        Retrieve the ItopapiServiceFamily related to this instance
        """
        if self.servicefamily_id is not None:
            return ItopapiPrototype.get_itop_class('ServiceFamily').find(self.servicefamily_id)
        return None

    def set_servicefamily(self, servicefamily):
        """
        Set the ItopapiServiceFamily parameters
        """
        self.servicefamily_id = servicefamily.instance_id
        self.servicefamily_id_friendlyname = servicefamily.friendlyname
        self.servicefamily_name = servicefamily.name
