def file_read(fname):
	from itertools import islice
	with open(fname,"a") as myfile:
		myfile.write("Python Exercise \n")
		myfile.write("Java exercises")
	txt=open(fname)
	print txt.read()

file_read('read.txt')
