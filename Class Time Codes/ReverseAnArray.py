t=int(input("Enter how many cases you want to test :"))
rev=[]

if t>=1 and t<=100:
	n=int(input("Enter the size of the aray :"))
	
	li = list(map(int, raw_input("Enter the array elements :").split()))	
	
	for i in range(0,n):
	        rev.append(li[n-(i+1)])

	print "The reversed array is :",
	for i in range(0,n):
		print (rev[i]),
else:
	print "Test case limit exeeded. Exiting."
	exit()

