# -*- coding: utf8 -*-fr
# pylint: disable=too-many-instance-attributes, invalid-name
"""
HasTeam is a mixin representing the team attached to some of the objects.
"""

from itopapi.model.prototype import ItopapiPrototype

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.fr>']


class HasTeam(object):
    """
    HasOrganization represents the organization attached to some top-level objects.
    """

    """ Configuration specific to itop """
    foreign_key = {'id': 'team_id', 'name': 'team_name', 'table': 'Team'}

    def __init__(self):
        super(HasTeam, self).__init__()

        # Object's team id. Call find_team to get the full information or just use
        # team_id_friendlyname and team_name
        self.team_id = None
        # Object's team id's friendly name. Not sure the difference with team_name
        self.team_id_friendlyname = None
        # Object's team name
        self.team_name = None

    def find_team(self):
        """
        Retrieve the ItopapiTeam related to this instance
        """
        if self.team_id is not None:
            return ItopapiPrototype.get_itop_class('Team').find(self.team_id)
        return None

    def set_team(self, team):
        """
        Set the ItopapiOrganization parameters
        """
        self.team_id = team.instance_id
        self.team_id_friendlyname = team.friendlyname
        self.team_name = team.name
