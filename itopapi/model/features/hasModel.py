# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasModel is a mixin representing the model attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasModel(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'model_id', 'name': 'model_name', 'table': 'Model'}

    def __init__(self):
        super(HasModel, self).__init__()

        # Object's model id. Call find_model to get the full information or just use
        # model_id_friendlyname and model_name
        self.model_id = None
        # Object's model id's friendly name. Not sure the difference with model_name
        self.model_id_friendlyname = None
        # Object's model name
        self.model_name = None

    def find_model(self):
        """
        Retrieve the ItopapiModel related to this instance
        """
        if self.model_id is not None:
            return ItopapiPrototype.get_itop_class('Model').find(self.location_id)
        return None

    def set_model(self, model):
        """
        Set the ItopapiModel parameters
        """
        self.model_id = model.instance_id
        self.model_id_friendlyname = model.friendlyname
        self.model_name = model.name
