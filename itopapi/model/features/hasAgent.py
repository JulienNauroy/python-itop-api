# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasAgent is a mixin representing the agent attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasAgent(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'agent_id', 'name': 'agent_name', 'table': 'Person'}

    def __init__(self):
        super(HasAgent, self).__init__()

        # Object's agent id. Call find_agent to get the full information or just use agent_name
        self.agent_id = None
        # Object's agent name
        self.agent_name = None

    def find_agent(self):
        """
        Retrieve the ItopapiAgent related to this instance
        """
        if self.agent_id is not None:
            return ItopapiPrototype.get_itop_class('Person').find(self.agent_id)
        return None

    def set_agent(self, agent):
        """
        Set the ItopapiOrganization parameters
        """
        self.agent_id = agent.instance_id
        self.agent_name = agent.name
