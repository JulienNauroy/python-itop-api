# python-itop-api
Python API to interface iTop to various other tools.
Three command-line scripts are currently provided: itop-cli, vcenter2itop and itop2centreon

## itop-cli
itop-cli is a generic CLI (command line interface) to the iTop REST interface.
You can use it to list the contents of iTop classes with the command

    user@machine> itop-cli --classes server rack
   
You can also search some specific instance with option --find

    user@machine> itop-cli --classes server --find host.domain.com
    
You can have a look at the options with the --help command

    user@machine> itop-cli --help
    
	usage: itop-cli [-h] [--hostname HOSTNAME] [--username USERNAME]
					[--password PASSWORD] [--organization ORGANIZATION-NAME]
					[--virtualhost VIRTUAL-HOSTNAME] [--config CONFIG_FILE]
					[--classes [ITOP-CLASS [ITOP-CLASS ...]]]
					[--find INSTANCE [INSTANCE ...]] [--delete] [--import-uri URI]
					[--import-stdin] [--format FORMAT] [--save]
					[--prevent-duplicates]

	python CLI for iTop REST api

	optional arguments:
	  -h, --help            show this help message and exit

	itop:
	  --hostname HOSTNAME   hostname of iTop server
	  --username USERNAME   username for iTop authentication
	  --password PASSWORD   password for iTop authentication
	  --organization ORGANIZATION-NAME
							iTop organization to use
	  --virtualhost VIRTUAL-HOSTNAME
							Itop's virtual host name for VMs

	cli:
	  --config CONFIG_FILE  configuration file CLI must use (default = ./itop-
							cli.cfg)
	  --classes [ITOP-CLASS [ITOP-CLASS ...]]
							iTop classes to use
	  --find INSTANCE [INSTANCE ...]
							Find and display information about a given class
							instance givenits name or ID
	  --delete              Delete all instances previously loaded
	  --save                Save the instances loaded through import
	  --prevent-duplicates  Check if objects with the same name already exist
							before savingand don't save in this case

	import:
	  --import-uri URI      URI of file to import
	  --import-stdin        import data from STDIN
	  --format FORMAT       Format of file you want import

	  
## vcenter2itop
vcenter2itop focuses on extracting data from a VMWare VCenter cluster and importing it into iTop.
It synchronises Farms, Servers, Hypervisors and VirtualMachines present in a VCenter as well as Brands, Models, OS Families and Versions.
It has a dependency on the pyVmomi module.

All parameters are set into the common python-itop-api.cfg script. vcenter2itop is then simply runs this way:

    user@machine> vcenter2itop

# itop2centreon
itop2centreon is an attempt at synchronizing iTop with the Centreon monitoring system through its CLAPI (command-line API) interface.
For now, it synchronizes the list of machines (Servers and VMs) and contacts.
It can serve as a kickstart script for your own synchronization mechanism.
