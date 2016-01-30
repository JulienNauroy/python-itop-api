# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasDeliveryModel is a mixin representing the deliverymodel attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasDeliveryModel(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'deliverymodel_id', 'name': 'deliverymodel_name', 'table': 'DeliveryModel'}

    def __init__(self):
        super(HasDeliveryModel, self).__init__()

        # Object's deliverymodel id. Call find_deliverymodel to get the full information or just use
        # deliverymodel_id_friendlyname and deliverymodel_name
        self.deliverymodel_id = None
        # Object's deliverymodel id's friendly name. Not sure the difference with deliverymodel_name
        self.deliverymodel_id_friendlyname = None
        # Object's deliverymodel name
        self.deliverymodel_name = None

    def find_deliverymodel(self):
        """
        Retrieve the ItopapiDeliveryModel related to this instance
        """
        if self.deliverymodel_id is not None:
            return ItopapiPrototype.get_itop_class('DeliveryModel').find(self.deliverymodel_id)
        return None

    def set_deliverymodel(self, deliverymodel):
        """
        Set the ItopapiOrganization parameters
        """
        self.deliverymodel_id = deliverymodel.instance_id
        self.deliverymodel_id_friendlyname = deliverymodel.friendlyname
        self.deliverymodel_name = deliverymodel.name
