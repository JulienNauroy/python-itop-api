# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasBrand is a mixin representing the brand attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasBrand(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'brand_id', 'name': 'brand_name', 'table': 'Brand'}

    def __init__(self):
        super(HasBrand, self).__init__()

        # Object's brand id. Call find_brand to get the full information or just use
        # brand_id_friendlyname and brand_name
        self.brand_id = None
        # Object's brand id's friendly name. Not sure the difference with brand_name
        self.brand_id_friendlyname = None
        # Object's brand name
        self.brand_name = None

    def find_brand(self):
        """
        Retrieve the ItopapiBrand related to this instance
        """
        if self.brand_id is not None:
            return ItopapiPrototype.get_itop_class('Brand').find(self.brand_id)
        return None

    def set_brand(self, brand):
        """
        Set the ItopapiBrand parameters
        """
        self.brand_id = brand.instance_id
        self.brand_id_friendlyname = brand.friendlyname
        self.brand_name = brand.name
