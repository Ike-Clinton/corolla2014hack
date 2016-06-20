#!/bin/bash
# Display usage parameters
display_usage() {
	echo "This script must be run as super-user."
	echo -e "\nUsage: \n$0 [arguments] \n"
}

if [ $# -le 1 ]
then
	display_usage
	exit 1
fi
# Check if user supplies --help or --h and show usage
if [[ ( $# == "--help") || $# == "-h"]]
then
	display_usage
	exit 0
fi
#Display usage if script not run as root/sudo
if [[$USER != "root"]]; 
then
	echo "This script must be run as super-user!"
	exit 1
fi
# Begin script
echo "All good!"
