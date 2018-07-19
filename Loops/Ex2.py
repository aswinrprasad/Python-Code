limit=input("Enter a number :")
if limit < 10 or limit > 100:
	print "Invalid input."
else:	
	print "The input number is divisible by :"
	for i in range(1,limit+1):
		if limit%(i)==0:
			print i

	
