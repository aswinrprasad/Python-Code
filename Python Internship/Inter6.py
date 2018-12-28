def test_prime(n):
	if n==1:
		print "Neither prime nor composite number"
		exit(0)	
	if n==2:
		flag=1 
	else:
		x=2
		while x <n+1 :
			if n%x==0:
				if n==x:
					flag=1
					break
				else:
					flag=0
					break
			else:
				flag=0
			x+=1
	
	if flag==1:
		print "Prime no."
	else:
		print "Not prime."

n=int(input("Enter a number to check if it is a prime no :"))
test_prime(n)

'''
		for x in range(2,n+1):
			if n%x==0:
				if n==x:
					flag=1
					break
				else:
					flag=0
					break
			else:
				flag=0
	'''
