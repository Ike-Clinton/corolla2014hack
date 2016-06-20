#!/bin/bash
# Display usage parameters
display_usage() {
	echo -e "\nUsage: \nsudo $0 \n"
}

if [ $# -ne 0 ]
then
	display_usage
	exit 1
fi
# Check if user supplies --help or --h and show usage
if [[ ( $# == "--help") || $# == "-h" ]]
then
	display_usage
	exit 0
fi
#Display usage if script not run as root/sudo
if [ "$EUID" -ne 0 ]
	then echo "This script must be run as super-user!"
	exit
fi
# Begin script

# Create virtual CAN interface
modprobe vcan
ip link add vcan0 type vcan
ip link set vcan0 up