#Write a python function to calculate the factorial of a number. The function accepts the number as arguments.

n=input("Enter a number to find factorial :")
def fact(n):
	fact1 = 1
	while n!=0:
		fact1*=n
		n-=1
	return fact1

print "The factorial is :",fact(n)


