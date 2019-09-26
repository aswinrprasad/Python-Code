#Write a Python function that takes a number as a parameter and check the number is prime or not.
#Error for input 1235. Contribute and correct the code.
def test_prime(n):
	if n==1 or n==2:
		return True 
	else:
		for x in range(2,n-1):
			if int(n%x)==0:
				return False
			else:
				return True

n=int(input("Enter a number to check if it is a prime no :"))
i=test_prime(n)
if i==True:
	print "Prime no."
else:
	print "Not prime."
