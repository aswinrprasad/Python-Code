count=0
limit=input("Enter a number :")
if limit < 10 or limit > 100:
	print "Invalid input."
else:	
	print "It is divisible by :"
	for i in range(1,limit):
		if limit%(i+1)==0:
			count=count+1			
			print i+1
if count > 2:
	print "Not a prime number."
else:
	print "It is a Prime number."

