# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasVirtualMachine is a mixin representing the virtualmachine attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasVirtualMachine(object):
    """
    HasVirtualMachine represents the VirtualMachine attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'virtualmachine_id', 'name': 'virtualmachine_name', 'table': 'VirtualMachine'}

    def __init__(self):
        super(HasVirtualMachine, self).__init__()

        # Object's virtualmachine id. Call find_virtualmachine to get the full information or just use
        # virtualmachine_id_friendlyname and virtualmachine_name
        self.virtualmachine_id = None
        # Object's virtualmachine id's friendly name. Not sure the difference with virtualmachine_name
        self.virtualmachine_id_friendlyname = None
        # Object's virtualmachine name
        self.virtualmachine_name = None

    def find_virtualmachine(self):
        """
        Retrieve the ItopapiVirtualMachine related to this instance
        """
        if self.virtualmachine_id is not None:
            return ItopapiPrototype.get_itop_class('VirtualMachine').find(self.virtualmachine_id)
        return None

    def set_virtualmachine(self, virtualmachine):
        """
        Set the ItopapiVirtualMachine parameters
        """
        self.virtualmachine_id = virtualmachine.instance_id
        self.virtualmachine_id_friendlyname = virtualmachine.friendlyname
        self.virtualmachine_name = virtualmachine.name
