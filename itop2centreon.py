#!/usr/bin/env python
# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
itop2centreon is a basic CLI interface to export itop data into centreon
"""

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.Fr>']

from itopapi import ItopapiController, ItopapiConfig, UnsupportedImportFormat
from itopcli import load_configuration_cli, ItopcliConfig, NeedMoreArgs
from itopapi.model import *
import subprocess;


def csv_to_dict(csv):
    lines = csv.splitlines()
    headers = lines.pop(0).split(';')
    dict = []
    for line in lines:
        dict_line = {}
        for i, val in enumerate(line.split(';')):
            dict_line[headers[i]] = val.decode('utf-8')
        dict.append(dict_line)
    return dict


def run_clapi_list_command(object):
    out, err = subprocess.Popen([ItopapiConfig.centreon_clapi_path,
                          '-u', ItopapiConfig.centreon_username,
                          '-p', ItopapiConfig.centreon_password,
                          '-o', object,
                          '-a', 'show'],
                         stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()
    return csv_to_dict(out)


def run_clapi_action_command(object, action, values):
    out, err = subprocess.Popen([ItopapiConfig.centreon_clapi_path,
                                 '-u', ItopapiConfig.centreon_username,
                                 '-p', ItopapiConfig.centreon_password,
                                 '-o', object,
                                 '-a', action,
                                 '-v', ';'.join(str(x.encode('utf-8')) for x in values)],
                                stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()
    if out == "":
        return True
    else:
        print "Error running action command:"
        print out
        exit(0)


def main():
    """
    Main function
    """

    ######################################
    # Load Itop & Centreon configuration #
    ######################################
    try:
        load_configuration_cli()
    except NeedMoreArgs as e:
        print "Error: {}".format(e.message)
        exit(1)


    ####################
    # Some value check #
    ####################
    if ItopapiConfig.username is None\
            or ItopapiConfig.password is None:
        print "Error: Itop Username/Password missing"
        exit(1)
    if ItopapiConfig.centreon_username is None\
            or ItopapiConfig.centreon_password is None\
            or ItopapiConfig.centreon_clapi_path is None:
        print "Error: Centreon Username/Password/Path missing"
        exit(1)

    controller = ItopapiController()


    ######################
    # Synchronize Teams #
    #####################
    print "Synchronizing Itop teams..."
    centreon_contact_groups = run_clapi_list_command("CG")
    itop_teams = ItopapiTeam.find_all()
    for team in itop_teams:
        group_exists = False
        for contact_group in centreon_contact_groups:
            # TODO contact_group.name or description? e.g.: "Guest" VS "Guest Group"
            if team.name == contact_group['name']: group_exists = True
        if not group_exists:
            print u"adding team {0} as a contact group".format(team.friendlyname.format('utf-8'))
            run_clapi_action_command('CG', 'add', [team.name, team.name + ' (from Itop)'])
    # TODO remove groups not in Itop and delete removed contacts (complete resync?)

    #######################
    # Synchronize Persons #
    #######################
    print "Synchronizing Itop persons..."
    centreon_contacts = run_clapi_list_command("contact")
    # Can't get persons from teamps since their email is not listed in team.persons_list
    itop_persons = ItopapiPerson.find_all()
    for person in itop_persons:
        # All persons should have an email
        if person.email is None or '@' not in person.email:
            continue

        contact_alias = person.email.split('@')[0]
        contact_exists = False
        for contact in centreon_contacts:
            if person.email == contact['email']: contact_exists = True
        if not contact_exists:
            print u"adding person {0} as a contact".format(person.friendlyname.format('utf-8'))
            run_clapi_action_command('contact', 'add', [person.friendlyname, contact_alias, person.email, '', '0', '1', 'en_US', 'ldap'])
        # In all cases, add the contact to the contacts list and set various parameters
        for team in person.team_list:
            run_clapi_action_command('CG', 'addcontact', [team.team_name, person.email.split('@')[0]])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'enable_notifications', '1'])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'hostnotifcmd', 'host-notify-by-email'])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'hostnotifopt', 'd,u,r'])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'svcnotifcmd', 'service-notify-by-email'])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'servicenotifopt', 'w,u,c,r,f'])




if __name__ == "__main__":
    main()
