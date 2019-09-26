#Program to read any number of lines from a text file.
def file_read_from_head(fname,nlines):
	from itertools import islice
	for line in islice(open(fname,"r"),nlines):
			print line,

file_read_from_head('read.txt',3)
