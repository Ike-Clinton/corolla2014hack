#! /usr/bin/python3
# find_unique_can.py
# Python script to find unique CAN frame IDs from a log file
# Can logs are of the form:
# (timestamp) interface ID#FFFFFFFFFFFFFFFF
# Where timestamp is of the form: 0000000000.000000
# Where interface is usually one of vcan0 or can0
# Where frame ID is 3 hex chars: FFF
# and the data length is up to 8 bytes in hex following a pound sign
# Example:
# (1436509053.650713) vcan0 19E#6FE1CB7DE2218456
import argparse
from collections import Counter

# Create argparser object to add command line args and help option
parser = argparse.ArgumentParser(
	description = 'This program takes in a a CAN data log file as input and prints'
	+ ' the unique can IDs that it finds',
	epilog = '',
	add_help = True)

# Add
parser.add_argument("-i", action = "store", dest="file",
					help = "log file to read in")

args = parser.parse_args()

with open(args.file, 'r') as myfile:
	text = myfile.readlines()

c = Counter(l.strip().split()[2][0:3] for l in text[0:len(text)-1])
for x in c.most_common():
	print(x)


