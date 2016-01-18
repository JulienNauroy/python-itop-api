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
import sys


# TODO I don't like this. Is there a more pythonic way?
itop_os_families = None
itop_os_versions = None
itop_farms = None
itop_hypervisors = None
# Link between a Host in VCenter and a Farm in iTop
host_to_farm = {}

# Retrieve the os family or create it if it doesn't exist
def get_os_family(os_family_name):
    if os_family_name is None or os_family_name == "":
        os_family_name = "Unknown"

    global itop_os_families
    os_family = itop_os_families.get(os_family_name)
    if os_family is None:
        os_family = ItopapiOSFamily()
        os_family.name = os_family_name
        os_family.save()
        itop_os_families[os_family_name] = os_family
    return os_family


# Retrieve the os version or create it if it doesn't exist
def get_os_version(os_family_id, os_version_name):
    if os_version_name is None or os_version_name == "":
        os_version_name = "Unknown"

    global itop_os_versions
    os_version = itop_os_versions.get((os_family_id, os_version_name))
    if os_version is None:
        os_version = ItopapiOSVersion()
        os_version.name = os_version_name
        os_version.osfamily_id = os_family_id
        os_version.save()
        itop_os_families[(os_family_id, os_version_name)] = os_version
    return os_version


# Retrieve the virtualhost (Hypervisor or Farm) or create it if it doesn't exist
def get_virtualhost(virtualhost_name, organization):
    if virtualhost_name is None or virtualhost_name == "":
        virtualhost_name = "Unknown"

    global itop_farms, itop_hypervisors
    farm = itop_farms.get(virtualhost_name)
    if farm is not None:
        return farm
    hypervisor = itop_hypervisors.get(virtualhost_name)
    if hypervisor is not None:
        return hypervisor
    # By default, create a farm and not an hypervisor.
    # Maybe add a configuration option somewhere
    farm = ItopapiFarm()
    farm.name = virtualhost_name
    # Set the organization
    farm.org_id = organization.instance_id
    farm.org_id_friendlyname = organization.friendlyname
    farm.organization_name = organization.name
    farm.save()
    itop_farms[virtualhost_name] = farm
    return farm


def create_itop_farm(cluster, organization):
    # Retrieve the relevant information from the cluster

    # Create the ItopapiFarm instance
    farm = ItopapiFarm()
    # Set the organization
    farm.org_id = organization.instance_id
    farm.org_id_friendlyname = organization.friendlyname
    farm.organization_name = organization.name
    # TODO where to get the ESXi version installed?
    # Set other fields
    farm.name = cluster.name
    # farm.status = "production"
    return farm


def create_itop_server(host, organization):
    # Retrieve the relevant information from the host
    config = host.summary.config
    hardware = host.hardware

    # Create the ItopapiServer
    server = ItopapiServer()
    # Set the organization
    server.org_id = organization.instance_id
    server.org_id_friendlyname = organization.friendlyname
    server.organization_name = organization.name
    # Set the OS family
    os_family = get_os_family("VMWare ESXi")
    server.osfamily_id = os_family.instance_id
    server.osfamily_id_friendlyname = os_family.friendlyname
    server.osfamily_name = os_family.name
    # TODO where to get the ESXi version installed?
    # Set other fields
    server.name = host.name
    server.cpu = hardware.cpuInfo.numCpuCores # or numCpuThreads
    server.ram = hardware.memorySize / 1048576
    # TODO summary.hardware.vendor and summary.hardware.model for brand and model
    # server.status = "production"
    return server


def create_itop_hypervisor(server):
    global host_to_farm
    # Create the ItopapiHypervisor
    hypervisor = ItopapiHypervisor()
    # Set the organization. Same at the server's one
    hypervisor.org_id = server.org_id
    hypervisor.org_id_friendlyname = server.friendlyname
    hypervisor.organization_name = server.name
    # Set the server
    hypervisor.server_id = server.instance_id
    hypervisor.server_id_friendlyname = server.friendlyname
    hypervisor.server_name = server.name
    # Set the farm if possible
    farm = host_to_farm.get(server.name)
    if farm is not None:
        hypervisor.farm_id = farm.instance_id
        hypervisor.farm_id_friendlyname = farm.friendlyname
        hypervisor.farm_name = farm.name
    # Set other fields
    hypervisor.name = server.name

    return hypervisor


def create_itop_vm(virtual_machine, organization):
    # Retrieve the relevant information from the virtual_machine
    config = virtual_machine.config
    guest = virtual_machine.guest

    # Create the ItopapiVirtualMachine instance
    vm = ItopapiVirtualMachine()
    # Set the organization
    vm.org_id = organization.instance_id
    vm.org_id_friendlyname = organization.friendlyname
    vm.organization_name = organization.name
    # Set the OS family
    os_family = get_os_family(guest.guestFamily)
    vm.osfamily_id = os_family.instance_id
    vm.osfamily_id_friendlyname = os_family.friendlyname
    vm.osfamily_name = os_family.name
    # Set the OS version
    os_version = get_os_version(vm.osfamily_id, guest.guestFullName)
    vm.osversion_id = os_version.instance_id
    vm.osversion_id_friendlyname = os_version.friendlyname
    vm.osversion_name = os_version.name
    # Set the virtual host (Hypervisor or Farm)
    host_name = virtual_machine.runtime.host.name
    virtualhost = get_virtualhost(host_name, organization)
    vm.virtualhost_id = virtualhost.instance_id
    vm.virtualhost_id_friendlyname = virtualhost.friendlyname
    vm.virtualhost_name = virtualhost.name

    # Set other fields
    # TODO check all values
    vm.name = virtual_machine.name
    vm.managementip = guest.ipAddress
    # TODO vm.status => implementation, obsolete, production, stock depending on ???
    # TODO use instanceUuid in description?
    # TODO 'move2production', 'description'
    vm.cpu = config.hardware.numCPU * (config.hardware.numCPU if config.hardware.numCPU else 1)
    vm.ram = config.hardware.memoryMB

    return vm


def main():
    """
    Main function
    """

    global itop_farms, itop_hypervisors, host_to_farm

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
        organization = ItopapiOrganization.find_by_name(ItopapiConfig.organization)
        if organization is None:
            print "Error: Default organization \"{}\"not found".format(ItopapiConfig.vcenter_vm_sync_mode)
            exit(1)

    controller = ItopapiController()

    # First get the OS families and versions
    global itop_os_families, itop_os_versions
    itop_os_families = dict((os_family.name, os_family) for os_family in ItopapiOSFamily.find_all())
    itop_os_versions = dict(((os_version.osfamily_id, os_version.name), os_version) for os_version in ItopapiOSVersion.find_all())

    ###############################
    #    Connection to VCenter    #
    ###############################
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

    ########################
    #  Get data from Itop  #
    ########################
    print "Retrieving existing data from iTop..."
    # Retrieve existing Itop VMs
    itop_farms = dict((farm.name, farm) for farm in ItopapiFarm.find_all())
    itop_hypervisors = dict((hypervisor.name, hypervisor) for hypervisor in ItopapiHypervisor.find_all())
    itop_vms = dict((vm.name, vm) for vm in ItopapiVirtualMachine.find_all())
    itop_servers = dict((server.name, server) for server in ItopapiServer.find_all())

    ##########################
    #  Synchronize Clusters  #
    ##########################
    print "Synchronizing VCenter Clusters with Itop Farms..."
    # cluster_names will be used for deleting itop farms
    cluster_names = set()

    # Get data from VCenter
    # vim.ResourcePool, vim.ComputeResource, vim.ClusterComputeResource, vim.
    container_view = vcenter_content.viewManager.CreateContainerView(
        vcenter_content.rootFolder, [vim.ClusterComputeResource], True)
    children = container_view.view
    for child in children:
        cluster_name = child.name
        cluster_names.add(cluster_name)
        itop_farm = itop_farms.get(cluster_name)
        if itop_farm is not None:
            if "update" in ItopapiConfig.vcenter_cluster_sync_mode:
                # TODO Update cluster
                print "Updated cluster %s" % cluster_name
        elif "add" in ItopapiConfig.vcenter_cluster_sync_mode:
            # Create the Farm
            itop_farm = create_itop_farm(child, organization)
            if itop_farm is not None:
                itop_farm.save()
                print "Added cluster %s" % cluster_name
        # Fill the host_to_farm dict with this cluster's hosts
        for host in child.host:
            host_to_farm[host.name] = itop_farm
    if "delete" in ItopapiConfig.vcenter_cluster_sync_mode:
        for farm_name in itop_farms.keys():
            if farm_name not in cluster_names:
                itop_farms[farm_name].delete()
                itop_farms.pop(farm_name)
                print "Deleted cluster %s" % farm_name

    #######################
    #  Synchronize Hosts  #
    #######################
    print "Synchronizing VCenter Hosts with Itop Servers..."
    # host_names will be used for deleting itop servers
    host_names = set()

    # Get data from VCenter
    container_view = vcenter_content.viewManager.CreateContainerView(
        vcenter_content.rootFolder, [vim.HostSystem], True)
    children = container_view.view
    for child in children:
        host_name = child.name
        host_names.add(host_name)
        itop_server = itop_servers.get(host_name)
        if itop_server is not None:
            if "update" in ItopapiConfig.vcenter_host_sync_mode:
                # TODO Update server
                print "Updated server %s" % host_name
        elif "add" in ItopapiConfig.vcenter_host_sync_mode:
            # Create the Server and Hyervisor
            server = create_itop_server(child, organization)
            if server is not None:
                server.save()
                hypervisor = create_itop_hypervisor(server)
                hypervisor.save()
                print "Added server %s" % host_name
    if "delete" in ItopapiConfig.vcenter_host_sync_mode:
        for server_name in itop_servers.keys():
            if server_name not in host_names:
                itop_servers[server_name].delete()
                itop_servers.pop(server_name)
                print "Deleted server %s" % server_name

    #####################
    #  Synchronize VMS  #
    #####################
    print "Synchronizing VCenter VMs with Itop..."
    # vm_names will be used for deleting itop vms
    vm_names = set()

    # Get data from VCenter
    container_view = vcenter_content.viewManager.CreateContainerView(
        vcenter_content.rootFolder, [vim.VirtualMachine], True)
    children = container_view.view
    for child in children:
        # Do not take templates into consideration
        if child.config.template:
            continue

        vm_name = child.name
        vm_names.add(vm_name)
        itop_vm = itop_vms.get(vm_name)
        if itop_vm is not None:
            if "update" in ItopapiConfig.vcenter_vm_sync_mode:
                # TODO Update VM
                print "Updated VM %s" % vm_name
        elif "add" in ItopapiConfig.vcenter_vm_sync_mode:
            # Create the VM
            # TODO does not save because the cluster is not defined.
            vm = create_itop_vm(child, organization)
            if vm is not None:
                vm.save()
                print "Added VM %s" % vm_name
    if "delete" in ItopapiConfig.vcenter_vm_sync_mode:
        for vm_name in itop_vms.keys():
            if vm_name not in vm_names:
                itop_vms[vm_name].delete()
                print "Deleted VM %s" % vm_name

    return 0


if __name__ == "__main__":
    main()
