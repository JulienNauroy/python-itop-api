# -*- coding: utf8 -*-fr

"""
Import all class needed
"""

__version__ = '1.0'
__authors__ = ['Guillaume Philippon <guillaume.philippon@lal.in2p3.fr>', 'Julien Nauroy <julien.nauroy@u-psud.fr>']

from itopapi.model.prototype import ItopapiPrototype, ItopapiUnimplementedMethod
from itopapi.model.organization import ItopapiOrganization
from itopapi.model.location import ItopapiLocation
from itopapi.model.contact import ItopapiContact
from itopapi.model.person import ItopapiPerson
from itopapi.model.team import ItopapiTeam
from itopapi.model.functionalCI import ItopapiFunctionalCI
from itopapi.model.physicalDevice import ItopapiPhysicalDevice
from itopapi.model.rack import ItopapiRack
from itopapi.model.enclosure import ItopapiEnclosure
from itopapi.model.connectableCI import ItopapiConnectableCI
from itopapi.model.datacenterDevice import ItopapiDatacenterDevice
from itopapi.model.server import ItopapiServer
from itopapi.model.sanSwitch import ItopapiSANSwitch
from itopapi.model.tapeLibrary import ItopapiTapeLibrary
from itopapi.model.applicationSolution import ItopapiApplicationSolution
from itopapi.model.businessProcess import ItopapiBusinessProcess
from itopapi.model.softwareInstance import ItopapiSoftwareInstance
from itopapi.model.dbserver import ItopapiDBServer
from itopapi.model.webServer import ItopapiWebServer
from itopapi.model.pcSoftware import ItopapiPCSoftware
from itopapi.model.middleware import ItopapiMiddleware
from itopapi.model.otherSoftware import ItopapiOtherSoftware
from itopapi.model.middlewareInstance import ItopapiMiddlewareInstance
from itopapi.model.databaseSchema import ItopapiDatabaseSchema
from itopapi.model.webServer import ItopapiWebServer
from itopapi.model.webApplication import ItopapiWebApplication
from itopapi.model.virtualDevice import ItopapiVirtualDevice
from itopapi.model.virtualMachine import ItopapiVirtualMachine
from itopapi.model.virtualHost import ItopapiVirtualHost
from itopapi.model.hypervisor import ItopapiHypervisor
from itopapi.model.farm import ItopapiFarm
from itopapi.model.licence import ItopapiLicence
from itopapi.model.osLicence import ItopapiOSLicence
from itopapi.model.softwareLicence import ItopapiSoftwareLicence
from itopapi.model.typology import ItopapiTypology
from itopapi.model.osFamily import ItopapiOSFamily
from itopapi.model.osVersion import ItopapiOSVersion
from itopapi.model.contactType import ItopapiContactType
from itopapi.model.contractType import ItopapiContractType
from itopapi.model.documentType import ItopapiDocumentType
from itopapi.model.brand import ItopapiBrand
from itopapi.model.iosVersion import ItopapiIOSVersion
from itopapi.model.model import ItopapiModel
from itopapi.model.networkDeviceType import ItopapiNetworkDeviceType
from itopapi.model.networkInterface import ItopapiNetworkInterface
from itopapi.model.ipInterface import ItopapiIPInterface
from itopapi.model.physicalInterface import ItopapiPhysicalInterface
from itopapi.model.logicalInterface import ItopapiLogicalInterface
from itopapi.model.fiberChannelInterface import ItopapiFiberChannelInterface
from itopapi.model.powerConnection import ItopapiPowerConnection
from itopapi.model.powerSource import ItopapiPowerSource
from itopapi.model.pdu import ItopapiPDU
from itopapi.model.service import ItopapiService
from itopapi.model.vlan import ItopapiVLAN
from itopapi.model.subnet import ItopapiSubnet
from itopapi.model.tape import ItopapiTape
from itopapi.model.incident import ItopapiIncident

# TODO partial list of missing classes, with no particular order and along with their inheritance hierarchy :
# Document
#   DocumentFile
#   DocumentNote
#   DocumentWeb
# DatacenterDevice (defined)
#   NetworkDevice
#   StorageSystem
#   NAS
# Patch
#   OSPatch
#   SoftwarePatch
# Group
# Contract
#   CustomerContract
#   ProviderContract
# ServiceFamily
# Service
# ServiceSubcategory
# SLA
# SLT
# DeliveryModel
# Contract
#   CustomerContract
#   ProviderContract
# NASFileSystem
# LogicalVolume

# Peripheral, MobilePhone, Printer, PC, Phone, IPPhone, Tablet, TapeLibrary, SANSwitchNAS
