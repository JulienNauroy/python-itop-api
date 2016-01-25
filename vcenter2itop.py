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
import json

# TODO a bug remains when creating a new OS Version ?!?


# Helper function to cleanup everything the script is supposed to add
# Do not use it in a mixed configuration
def cleanup():
    for x in ItopapiVirtualMachine.find_all():
        x.delete()
    for x in ItopapiHypervisor.find_all():
        x.delete()
    for x in ItopapiServer.find_all():
        x.delete()
    for x in ItopapiModel.find_all():
        x.delete()
    for x in ItopapiBrand.find_all():
        x.delete()
    for x in ItopapiOSVersion.find_all():
        x.delete()
    for x in ItopapiOSFamily.find_all():
        x.delete()
    exit(0)


# Helper function to get read of None values
def xstr(s):
    return u'' if s is None else (s if type(s) is unicode else unicode(s, "utf-8"))


# Global variables called here and there
itop_os_families = None
itop_os_versions = None
itop_farms = None
itop_hypervisors = None
itop_brands = None
itop_models = None
# Link between a Host in VCenter and a Farm in iTop
host_to_farm = {}


# Retrieve the os family or create it if it doesn't exist
def get_os_family(os_family_name):
    if xstr(os_family_name) == "":
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
def get_os_version(os_family, os_version_name):
    if xstr(os_version_name) == "":
        os_version_name = "Unknown"

    global itop_os_versions
    os_version = itop_os_versions.get((os_family.instance_id, os_version_name))
    if os_version is None:
        os_version = ItopapiOSVersion()
        os_version.name = os_version_name
        os_version.osfamily_id = os_family.instance_id
        os_version.osfamily_name = os_family.name
        os_version.osfamily_id_friendlyname = os_family.friendlyname
        ret = os_version.save()
        itop_os_versions[(os_family.instance_id, os_version.name)] = os_version
    return os_version


# Retrieve the brand or create it if it doesn't exist
def get_brand(brand_name):
    if xstr(brand_name) == "":
        brand_name = "Unknown"

    global itop_brands
    itop_brand = itop_brands.get(brand_name)
    if itop_brand is None:
        itop_brand = ItopapiBrand()
        itop_brand.name = brand_name
        itop_brand.save()
        itop_brands[brand_name] = itop_brand
    return itop_brand


# Retrieve the model or create it if it doesn't exist
def get_model(brand, model_name, model_type):
    if xstr(model_name) == "":
        model_name = "Unknown"

    global itop_models
    itop_model = itop_models.get((brand.instance_id, model_name))
    if itop_model is None:
        itop_model = ItopapiModel()
        itop_model.name = model_name
        itop_model.type = model_type
        itop_model.brand_id = brand.instance_id
        itop_model.brand_id_friendlyname = brand.friendlyname
        itop_model.brand_name = brand.name
        itop_model.save()
        itop_models[(brand.instance_id, model_name)] = itop_model
    return itop_model


# Retrieve the virtualhost (Hypervisor or Farm) or create it if it doesn't exist
def get_virtualhost(virtualhost_name, organization):
    if xstr(virtualhost_name) == "":
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


# Fill data of a VCenter's Cluster into an ItopapiFarm instance
# Return true if anything changed, else return false
def get_farm_params(itop_farm, vcenter_cluster, organization):
    # Retrieve the relevant information from the cluster

    # Recall if there was a change in the params
    has_changed = False
    # Set the organization
    if itop_farm.org_id != organization.instance_id:
        has_changed = True
        itop_farm.org_id = organization.instance_id
        itop_farm.org_id_friendlyname = organization.friendlyname
        itop_farm.organization_name = organization.name
    # Set other fields
    if itop_farm.name != vcenter_cluster.name:
        has_changed = True
        itop_farm.name = vcenter_cluster.name
        # farm.status = "production"
    return has_changed


# Fill data of a VCenter's Host into an ItopapiServer instance
# Return true if anything changed, else return false
def get_server_params(itop_server, vcenter_host, organization):
    # Retrieve the relevant information from the host
    summary = vcenter_host.summary
    # config = summary.config
    hardware = vcenter_host.hardware
    product = vcenter_host.config.product

    # Recall if there was a change in the params
    has_changed = False
    # Set the management IP
    management_ip = xstr(summary.managementServerIp)
    if itop_server.managementip != management_ip:
        has_changed = True
        itop_server.managementip = management_ip
    # Set the organization
    if itop_server.org_id != organization.instance_id:
        has_changed = True
        itop_server.org_id = organization.instance_id
        itop_server.org_id_friendlyname = organization.friendlyname
        itop_server.organization_name = organization.name
    # Set the OS family
    os_family = get_os_family(product.name)
    if itop_server.osfamily_id != os_family.instance_id:
        has_changed = True
        itop_server.osfamily_id = os_family.instance_id
        itop_server.osfamily_id_friendlyname = os_family.friendlyname
        itop_server.osfamily_name = os_family.name
    # Set the OS version
    os_version = get_os_version(os_family, product.fullName)
    if itop_server.osversion_id != os_version.instance_id:
        has_changed = True
        itop_server.osversion_id = os_version.instance_id
        itop_server.osversion_id_friendlyname = os_version.friendlyname
        itop_server.osversion_name = os_version.name
    # Set the brand
    itop_brand = get_brand(summary.hardware.vendor)
    if itop_server.brand_id != itop_brand.instance_id:
        has_changed = True
        itop_server.brand_id = itop_brand.instance_id
        itop_server.brand_id_friendlyname = itop_brand.friendlyname
        itop_server.brand_name = itop_brand.name
    # Set the model
    itop_model = get_model(itop_brand, summary.hardware.model, "Server")
    if itop_server.model_id != itop_model.instance_id:
        has_changed = True
        itop_server.model_id = itop_model.instance_id
        itop_server.model_id_friendlyname = itop_model.friendlyname
        itop_server.model_name = itop_model.name
    # TODO where to get the ESXi version installed?
    # Set other fields
    cpu_count = int(hardware.cpuInfo.numCpuCores * hardware.cpuInfo.numCpuPackages)
    if itop_server.name != vcenter_host.name \
            or int(itop_server.cpu) != cpu_count \
            or int(itop_server.ram) != int(hardware.memorySize / 1048576):
        has_changed = True
        itop_server.name = vcenter_host.name
        itop_server.cpu = cpu_count
        itop_server.ram = int(hardware.memorySize / 1048576)

    return has_changed


# Set params of an ItoapiHypervisor using data from the ItopapiServer.
# By convention, the hypervisor will have the same name.
def get_hypervisor_params(itop_hypervisor, itop_server):
    global host_to_farm
    # Set the organization. Same at the server's one
    itop_hypervisor.org_id = itop_server.org_id
    itop_hypervisor.org_id_friendlyname = itop_server.friendlyname
    itop_hypervisor.organization_name = itop_server.name
    # Set the server
    itop_hypervisor.server_id = itop_server.instance_id
    itop_hypervisor.server_id_friendlyname = itop_server.friendlyname
    itop_hypervisor.server_name = itop_server.name
    # Set the farm if possible
    farm = host_to_farm.get(itop_server.name)
    if farm is not None:
        itop_hypervisor.farm_id = farm.instance_id
        itop_hypervisor.farm_id_friendlyname = farm.friendlyname
        itop_hypervisor.farm_name = farm.name
    # Set other fields
    itop_hypervisor.name = itop_server.name

    return itop_hypervisor


# Fill data of a VCenter's VirtualMachine into an ItopapiVirtualMachine instance
# Return true if anything changed, else return false
def get_vm_params(itop_vm, vcenter_vm, organization):
    # Retrieve the relevant information from the virtual_machine
    config = vcenter_vm.config
    guest = vcenter_vm.guest
    os_family = get_os_family(guest.guestFamily)
    os_version = get_os_version(os_family, guest.guestFullName)
    host_name = vcenter_vm.runtime.host.name
    virtualhost = get_virtualhost(host_name, organization)

    # Recall if there was a change in the params
    has_changed = itop_vm.org_id != organization.instance_id \
                    or itop_vm.osfamily_id != os_family.instance_id \
                    or itop_vm.osversion_id != os_version.instance_id \
                    or itop_vm.virtualhost_id != virtualhost.instance_id
    # Set the organization
    itop_vm.org_id = organization.instance_id
    itop_vm.org_id_friendlyname = organization.friendlyname
    itop_vm.organization_name = organization.name
    # Set the OS family
    itop_vm.osfamily_id = os_family.instance_id
    itop_vm.osfamily_id_friendlyname = os_family.friendlyname
    itop_vm.osfamily_name = os_family.name
    # Set the OS version
    itop_vm.osversion_id = os_version.instance_id
    itop_vm.osversion_id_friendlyname = os_version.friendlyname
    itop_vm.osversion_name = os_version.name
    # Set the virtual host (Hypervisor or Farm)
    itop_vm.virtualhost_id = virtualhost.instance_id
    itop_vm.virtualhost_id_friendlyname = virtualhost.friendlyname
    itop_vm.virtualhost_name = virtualhost.name

    # Set other fields
    config_cpu = int(config.hardware.numCPU)
    ip_address = xstr(guest.ipAddress)

    if itop_vm.name != vcenter_vm.name \
            or itop_vm.managementip != ip_address \
            or int(itop_vm.cpu) != config_cpu \
            or int(itop_vm.ram) != int(config.hardware.memoryMB):
        has_changed = True
        itop_vm.name = vcenter_vm.name
        itop_vm.managementip = ip_address
        itop_vm.cpu = config_cpu
        itop_vm.ram = config.hardware.memoryMB

    # Set extra values as a JSON array inside the description field
    current_desc = {}
    try:
        current_desc = json.loads(xstr(itop_vm.description))
    except ValueError as e:
        pass
    vcenter_hostname = xstr(vcenter_vm.guest.hostName)
    if xstr(current_desc.get("hostname")) != vcenter_hostname:
        has_changed = True
        current_desc['hostname'] = vcenter_hostname
    vcenter_annotation = xstr(vcenter_vm.config.annotation)
    if xstr(current_desc.get("annotation")) != vcenter_annotation:
        has_changed = True
        current_desc['annotation'] = vcenter_annotation

    itop_vm.description = json.dumps(current_desc)

    return has_changed


def main():
    """
    Main function
    """

    global itop_farms, itop_hypervisors, host_to_farm, itop_brands, itop_models, itop_os_families, itop_os_versions

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

    ###############################
    #    Connection to VCenter    #
    ###############################
    ssl_context = None
    if ItopapiConfig.vcenter_unsecure:
        ssl_context = ssl._create_unverified_context()

    vcenter_content = None

    try:
        if xstr(ItopapiConfig.vcenter_password) == "":
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
    itop_os_families = dict((os_family.name, os_family) for os_family in ItopapiOSFamily.find_all())
    itop_os_versions = dict(((os_version.osfamily_id, os_version.name), os_version) for os_version in ItopapiOSVersion.find_all())
    itop_brands = dict((brand.name, brand) for brand in ItopapiBrand.find_all())
    itop_models = dict(((model.brand_id, model.name), model) for model in ItopapiModel.find({"type": "Server"}))

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
    for vcenter_cluster in container_view.view:
        cluster_name = vcenter_cluster.name
        cluster_names.add(cluster_name)
        itop_farm = itop_farms.get(cluster_name)
        if itop_farm is not None:
            if "update" in ItopapiConfig.vcenter_cluster_sync_mode:
                has_changed = get_farm_params(itop_farm, vcenter_cluster, organization)
                if has_changed:
                    ret = itop_farm.save()
                    if ret['code'] == 0:
                        print "Updated cluster %s" % cluster_name
                    else:
                        print "ERROR: cluster %s could not be updated. Check the return code below." % cluster_name
                        print ret
        elif "add" in ItopapiConfig.vcenter_cluster_sync_mode:
            itop_farm = ItopapiFarm()
            get_farm_params(itop_farm, vcenter_cluster, organization)
            ret = itop_farm.save()
            if ret['code'] == 0:
                print "Added cluster %s" % cluster_name
            else:
                print "ERROR: cluster %s could not be added. Check the return code below." % cluster_name
                print ret

        # Fill the host_to_farm dict with this cluster's hosts
        for host in vcenter_cluster.host:
            host_to_farm[host.name] = itop_farm
    if "delete" in ItopapiConfig.vcenter_cluster_sync_mode:
        for farm_name in itop_farms.keys():
            if farm_name not in cluster_names:
                ret = itop_farms[farm_name].delete()
                itop_farms.pop(farm_name)
                if ret['code'] == 0:
                    print "Deleted cluster %s" % farm_name
                else:
                    print "ERROR: cluster %s could not be deleted. Check the return code below." % farm_name
                    print ret

    #######################
    #  Synchronize Hosts  #
    #######################
    print "Synchronizing VCenter Hosts with Itop Servers..."
    # host_names will be used for deleting itop servers
    host_names = set()

    # Get data from VCenter
    container_view = vcenter_content.viewManager.CreateContainerView(
        vcenter_content.rootFolder, [vim.HostSystem], True)
    for vcenter_host in container_view.view:
        host_name = vcenter_host.name
        host_names.add(host_name)
        itop_server = itop_servers.get(host_name)
        if itop_server is not None:
            if "update" in ItopapiConfig.vcenter_host_sync_mode:
                has_changed = get_server_params(itop_server, vcenter_host, organization)
                if has_changed:
                    ret = itop_server.save()
                    if ret['code'] == 0:
                        print "Updated server %s" % host_name
                    else:
                        print "ERROR: server %s could not be updated. Check the return code below." % host_name
                        print ret
        elif "add" in ItopapiConfig.vcenter_host_sync_mode:
            # Create the Server and Hypervisor
            itop_server = ItopapiServer()
            get_server_params(itop_server, vcenter_host, organization)
            ret = itop_server.save()
            if ret['code'] == 0:
                itop_hypervisor = ItopapiHypervisor()
                get_hypervisor_params(itop_hypervisor, itop_server)
                ret = itop_hypervisor.save()
                if ret['code'] == 0:
                    print "Added server %s" % host_name
                else:
                    print "ERROR: hypervisor %s could not be created. Check the return code below." % host_name
            else:
                print "ERROR: server %s could not be created. Check the return code below." % host_name
                print ret
    if "delete" in ItopapiConfig.vcenter_host_sync_mode:
        for server_name in itop_servers.keys():
            if server_name not in host_names:
                ret = itop_servers[server_name].delete()
                itop_servers.pop(server_name)
                if ret['code'] == 0:
                    print "Deleted server %s" % server_name
                else:
                    print "ERROR: server %s could not be deleted. Check the return code below." % server_name
                    print ret


    #####################
    #  Synchronize VMS  #
    #####################
    print "Synchronizing VCenter VMs with Itop..."
    # vm_names will be used for deleting itop vms
    vm_names = set()

    # Get data from VCenter
    container_view = vcenter_content.viewManager.CreateContainerView(
        vcenter_content.rootFolder, [vim.VirtualMachine], True)
    for vcenter_vm in container_view.view:
        # Do not take templates into consideration
        if vcenter_vm.config.template:
            continue

        vm_name = vcenter_vm.name
        vm_names.add(vm_name)
        itop_vm = itop_vms.get(vm_name)
        if itop_vm is not None:
            if "update" in ItopapiConfig.vcenter_vm_sync_mode:
                has_changed = get_vm_params(itop_vm, vcenter_vm, organization)
                if has_changed:
                    ret = itop_vm.save()
                    if ret['code'] == 0:
                        print "Updated VM %s" % vm_name
                    else:
                        print "ERROR: VM %s could not be updated. Check the return code below." % vm_name
                        print ret
        elif "add" in ItopapiConfig.vcenter_vm_sync_mode:
            itop_vm = ItopapiVirtualMachine()
            get_vm_params(itop_vm, vcenter_vm, organization)
            ret = itop_vm.save()
            if ret['code'] == 0:
                print "Added VM %s" % vm_name
            else:
                print "ERROR: VM %s could not be created. Check the return code below." % vm_name
                print ret
    if "delete" in ItopapiConfig.vcenter_vm_sync_mode:
        for vm_name in itop_vms.keys():
            if vm_name not in vm_names:
                ret = itop_vms[vm_name].delete()
                if ret['code'] == 0:
                    print "Deleted VM %s" % vm_name
                else:
                    print "ERROR: VM %s could not be deleted. Check the return code below." % vm_name
                    print ret

    return 0


if __name__ == "__main__":
    main()
