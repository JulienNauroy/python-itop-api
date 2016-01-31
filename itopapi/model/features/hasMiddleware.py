# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasMiddleware is a mixin representing the middleware attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasMiddleware(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'middleware_id', 'name': 'middleware_name', 'table': 'Middleware'}

    def __init__(self):
        super(HasMiddleware, self).__init__()

        # Object's middleware id. Call find_middleware to get the full information or just use
        # middleware_id_friendlyname and middleware_name
        self.middleware_id = None
        # Object's middleware id's friendly name. Not sure the difference with middleware_name
        self.middleware_id_friendlyname = None
        # Object's middleware name
        self.middleware_name = None

    def find_middleware(self):
        """
        Retrieve the ItopapiMiddleware related to this instance
        """
        if self.middleware_id is not None:
            return ItopapiPrototype.get_itop_class('Middleware').find(self.middleware_id)
        return None

    def set_middleware(self, middleware):
        """
        Set the ItopapiMiddleware parameters
        """
        self.middleware_id = middleware.instance_id
        self.middleware_id_friendlyname = middleware.friendlyname
        self.middleware_name = middleware.name
