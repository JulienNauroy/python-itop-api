# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasDatacenterDevice is a mixin representing the datacenterdevice attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasDatacenterDevice(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'datacenterdevice_id', 'name': 'datacenterdevice_name', 'table': 'DatacenterDevice'}

    def __init__(self):
        super(HasDatacenterDevice, self).__init__()

        # Object's datacenterdevice id. Call find_datacenterdevice to get the full information or just use
        # datacenterdevice_id_friendlyname and datacenterdevice_name
        self.datacenterdevice_id = None
        # Object's datacenterdevice id's friendly name. Not sure the difference with datacenterdevice_name
        self.datacenterdevice_id_friendlyname = None
        # Object's datacenterdevice name
        self.datacenterdevice_name = None

    def find_datacenterdevice(self):
        """
        Retrieve the ItopapiDatacenterDevice related to this instance
        """
        if self.datacenterdevice_id is not None:
            return ItopapiPrototype.get_itop_class('DatacenterDevice').find(self.datacenterdevice_id)
        return None

    def set_datacenterdevice(self, datacenterdevice):
        """
        Set the ItopapiDatacenterDevice parameters
        """
        self.datacenterdevice_id = datacenterdevice.instance_id
        self.datacenterdevice_id_friendlyname = datacenterdevice.friendlyname
        self.datacenterdevice_name = datacenterdevice.name
