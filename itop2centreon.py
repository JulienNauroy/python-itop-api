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
import subprocess


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


def run_clapi_action_command(obj, action, values):
    out, err = subprocess.Popen([ItopapiConfig.centreon_clapi_path,
                                 '-u', ItopapiConfig.centreon_username,
                                 '-p', ItopapiConfig.centreon_password,
                                 '-o', obj,
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


    #####################
    # Synchronize Teams #
    #####################
    print "Synchronizing Itop teams / Centreon contact groups..."
    centreon_contact_groups = run_clapi_list_command("CG")
    itop_teams = ItopapiTeam.find_all()
    for team in itop_teams:
        group_exists = False
        for contact_group in centreon_contact_groups:
            if team.name == contact_group['name']: group_exists = True
        if not group_exists:
            print u"adding team {0} as a contact group".format(team.friendlyname.format('utf-8'))
            run_clapi_action_command('CG', 'add', [team.name, team.name + ' (from Itop)'])

    ###################################
    # Cleanup Centreon Contact Groups #
    ###################################
    print "Cleaning up Centreon contact groups..."
    all_contact_group_names = map(lambda s: s.name, itop_teams)
    for contact_group in centreon_contact_groups:
        if contact_group['name'] not in all_contact_group_names and contact_group['name'] != 'Supervisors':
            print u"deleting contact group {0} as is is not defined in itop".format(contact_group['name'].format('utf-8'))
            run_clapi_action_command('CG', 'DEL', [contact_group['name']])

    #######################
    # Synchronize Persons #
    #######################
    print "Synchronizing Itop persons / Centreon contacts..."
    centreon_contacts = run_clapi_list_command("contact")
    # Can't get persons from teams since their email is not listed in team.persons_list
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
            run_clapi_action_command('CG', 'addcontact', [team.team_name, contact_alias])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'enable_notifications', '1'])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'hostnotifcmd', 'host-notify-by-email'])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'hostnotifopt', 'd,u,r'])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'svcnotifcmd', 'service-notify-by-email'])
        run_clapi_action_command('contact', 'setParam', [contact_alias, 'servicenotifopt', 'w,u,c,r,f'])

    #############################
    # Cleanup Centreon Contacts #
    #############################
    print "Cleaning up Centreon contacts..."
    all_contact_aliases = map(lambda s: '' if s.email is None else s.email.split('@')[0], itop_persons)
    for contact in centreon_contacts:
        if contact['alias'] not in all_contact_aliases and contact['alias'] != 'admin':
            print u"deleting contact {0} as is is not defined in itop".format(contact['alias'].format('utf-8'))
            run_clapi_action_command('contact', 'DEL', [contact['alias']])

    def sync_servers(servers, centreon_hosts):
        for server in servers:
            if server.managementip is None or server.managementip == '':
                continue
            server_exists = False
            for host in centreon_hosts:
                if server.name == host['name']: server_exists = True
            if server.status != 'production':
                if server_exists:
                    # Remove servers no longer in production
                    print u"removing {0} as a host as its status is {1}".format(server.name.format('utf-8'), server.status)
                    run_clapi_action_command('HOST', 'DEL', [server.name])
                continue

            if not server_exists:
                print u"adding {0} as a host".format(server.name.format('utf-8'))
                run_clapi_action_command('HOST', 'ADD', [server.name, server.description, server.managementip,
                                                         'generic-host', 'central', ''])

            # Set the server parameters
            run_clapi_action_command('HOST', 'setParam', [server.name, 'check_period', '24x7'])
            # Set the contacts
            for contact in server.contacts_list:
                if type(contact) is ItopapiTeam:
                    run_clapi_action_command('HOST', 'addContactGroup', [server.name, contact.contact_name])
                else:
                    run_clapi_action_command('HOST', 'addContact', [server.name, contact.contact_id_friendlyname])

    #######################
    # Synchronize Servers #
    #######################
    print "Synchronizing Itop servers / Centreon hosts..."
    centreon_hosts = run_clapi_list_command("HOST")
    itop_servers = ItopapiServer.find_all()
    sync_servers(itop_servers, centreon_hosts)

    ###############################
    # Synchronize VirtualMachines #
    ###############################
    print "Synchronizing Itop VMs / Centreon hosts..."
    itop_vms = ItopapiVirtualMachine.find_all()
    sync_servers(itop_vms, centreon_hosts)

    ##########################
    # Cleanup Centreon Hosts #
    ##########################
    print "Cleaning up Centreon hosts..."
    all_servers_names = map(lambda s: s.name, itop_servers + itop_vms)
    for host in centreon_hosts:
        if host['name'] not in all_servers_names:
            print u"deleting host {0} as is is not defined in itop".format(host['name'].format('utf-8'))
            run_clapi_action_command('HOST', 'DEL', [host['name']])

    return 0


if __name__ == "__main__":
    main()
