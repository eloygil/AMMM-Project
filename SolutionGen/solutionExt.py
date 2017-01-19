'''
AMMM Python Solver Solution Extractor v1.0
Copyright 2016 Eloy Gil.
'''

import sys

if __name__ == '__main__':
	print 'Exporting solutions: \n'
	search_str = "NT: "
	search_str2 = "Q: "
	lines = [] # Declare an empty list named "lines"
	filename = sys.argv[1]
	with open (filename, 'rt') as in_file: # Open file argv[1] to read data.
		print "NT: "
		val = []
		for line in in_file:
			if search_str in line:
				print int(line.split(search_str)[1].split(search_str2)[0])
				val.append(int(line.split(search_str)[1].split(search_str2)[1]))
		print "Q: "
		for v in val:
			print v