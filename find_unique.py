#! /usr/bin/python3
# find_unique.py
# By Ike Clinton

# Python script to count CAN frame IDs from a log file
# Can logs are of the form:
# (timestamp) interface ID#FFFFFFFFFFFFFFFF
# Where timestamp is of the form: 0000000000.000000
# Where interface is usually one of vcan0 or can0
# Where frame ID is 3 hex chars: FFF
# and the data length is up to 8 bytes in hex following a pound sign
# Example:
# (1436509053.650713) vcan0 19E#6FE1CB7DE2218456
import argparse
import re
import os
from collections import Counter

# Create regex to match log files
logpattern = re.compile("*\.log")

# Create argparser object to add command line args and help option
parser = argparse.ArgumentParser(
	description = 'This program takes in a a CAN data log file as input and prints'
	+ ' the unique can IDs that it finds',
	epilog = '',
	add_help = True)

# Add a "-i" argument to receive a filename
parser.add_argument("-i", action = "store", dest="file",
					help = "log file to read in")

# Add a "-d" argument to receive a filename
parser.add_argument("-d", action = "store_const", dest="directory",
					help = "directory containing log files")

# Split and process arguments into "args"
args = parser.parse_args()

def analyze_file():
	# Open the file as read only, read the lines into text
	with open(args.file, 'r') as myfile:
		text = myfile.readlines()

	# Strip newlines, and split on spaces
	# Select the first 3 characters (the frame ids) and count them
	# Finally, use most_common() to display them decreasing order
	c = Counter(l.strip().split()[2][0:3] for l in text[0:len(text)-1])
	for x in c.most_common():
		print(x)

def analyze_dir():
	# loop through files in the given directory
	for fn in os.listdir(directory):
		if os.path.isfile(fn) and pattern.match(fn.filename):
			# Open the file as read only, read the lines into text
			with open(args.file, 'r') as myfile:
			text = myfile.readlines()