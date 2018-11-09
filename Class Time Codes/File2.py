#Program to write to a file.

def file_read(fname):
	from itertools import islice
	x=open(fname,"a")
	x.write("Python Exercise \n")
	x.write("Java exercises\n")
	txt=open(fname)
	print txt.read()

file_read('read.txt')
