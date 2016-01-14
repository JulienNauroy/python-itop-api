#!/usr/bin/env python
# -*- coding: utf8 -*-fr
# pylint: disable=invalid-name
"""
vcenter2itop is a basic CLI interface to export vcenter data into itop.
uses pyvmomi
"""

__version__ = '1.0'
__authors__ = ['Julien Nauroy <julien.nauroy@u-psud.Fr>']

from itopapi import ItopapiController, ItopapiConfig, UnsupportedImportFormat
from itopcli import load_configuration_cli, ItopcliConfig, NeedMoreArgs
from itopapi.model import *
from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim
import ssl
import getpass
import atexit


def create_itop_vm(virtual_machine, organization):
    # Retrieve the relevant information from the virtual_machine
    config = virtual_machine.config
    guest = virtual_machine.guest
    # Create the ItopVirtualMachine instance
    vm = ItopapiVirtualMachine()
    # Set the organization
    vm.org_id = organization.instance_id
    vm.org_id_friendlyname = organization.friendlyname
    vm.organization_name = organization.name
    # Set other fields
    # TODO check all values
    vm.name = config.name
    vm.managementip = guest.ipAddress
    # TODO vm.status => implementation, obsolete, production, stock depending on ???
    # TODO OS Licence
    # TODO use instanceUuid in description?
    vm.cpu = config.hardware.numCPU * (config.hardware.numCPU if config.hardware.numCPU else 1)
    vm.ram = config.hardware.memoryMB
    # TODO get or create guest.guestFamily (windowsGuest, linuxGuest or None) and guest.guestFullName
    #print guest.guestFullName
    # TODO 'move2production', 'description'

    return vm


def main():
    """
    Main function
    """

    ######################################
    # Load Itop & pyvmomi configuration #
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

    if ItopapiConfig.vcenter_username is None\
            or ItopapiConfig.vcenter_host is None\
            or ItopapiConfig.vcenter_port is None:
        print "Error: VCenter Host/Port/Username missing"
        exit(1)

    for m in ItopapiConfig.vcenter_vm_sync_mode:
        if m not in ["add", "update", "delete"]:
            print "Error: unsupported vm sync mode {}".format(m)
            exit(1)
    if ItopapiConfig.organization is None or ItopapiConfig.organization == "" \
            and "add" in ItopapiConfig.vcenter_vm_sync_mode:
        print "Error: Default organization missing"
        exit(1)
    # Retrieve the default organization if need be
    organization = None
    if "add" in ItopapiConfig.vcenter_vm_sync_mode:
        find_organization = ItopapiOrganization.find_by_name(ItopapiConfig.organization)
        if find_organization is None:
            print "Error: Default organization \"{}\"not found".format(ItopapiConfig.vcenter_vm_sync_mode)
            exit(1)
        else:
            # Only one result
            organization = find_organization[0]

    controller = ItopapiController()

    #####################
    #    Connection     #
    #####################
    ssl_context = None
    if ItopapiConfig.vcenter_unsecure:
        ssl_context = ssl._create_unverified_context()
    vcenter_content = None

    try:
        if ItopapiConfig.vcenter_password is None or ItopapiConfig.vcenter_password == "":
            ItopapiConfig.vcenter_password = getpass.getpass()
        service_instance = connect.SmartConnect(sslContext=ssl_context,
                                                host=ItopapiConfig.vcenter_host,
                                                user=ItopapiConfig.vcenter_username,
                                                pwd=ItopapiConfig.vcenter_password,
                                                port=ItopapiConfig.vcenter_port)

        atexit.register(connect.Disconnect, service_instance)

        vcenter_content = service_instance.RetrieveContent()

    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return -1

    # TODO physical and storage servers, if possible
    # TODO in the configuration, have the choice between add,update,delete to define the synchronization level

    #####################
    #  Synchronize VMS  #
    #####################
    print "Synchronizing VCenter VMs with Itop..."
    # Retrieve existing Itop VMs
    itop_vms = dict((vm.name, vm) for vm in ItopapiVirtualMachine.find_all())

    # First get the OS families and versions
    itop_os_families = ItopapiOSFamily.find_all()
    itop_os_versions = ItopapiOSVersion.find_all()
    # TODO create OS families and versions if not exist and update VMs
    # Get data from VCenter
    container = vcenter_content.rootFolder  # starting point to look into
    view_type = [vim.VirtualMachine]  # object types to look for
    recursive = True  # whether we should look into it recursively
    container_view = vcenter_content.viewManager.CreateContainerView(
        container, view_type, recursive)

    children = container_view.view
    for child in children:
        vm_name = child.config.name
        itop_vm = itop_vms.get(vm_name)
        if itop_vm is not None:
            if "update" in ItopapiConfig.vcenter_vm_sync_mode:
                # TODO Update VM
                2+2
        elif "add" in ItopapiConfig.vcenter_vm_sync_mode:
            # Create the VM
            vm = create_itop_vm(child, organization)
            # TODO does not save?
            vm.save()
            print "Added VM %s" % vm_name
    if "delete" in ItopapiConfig.vcenter_vm_sync_mode:
        # TODO
        2+2

    return 0


if __name__ == "__main__":
    main()
