#Write a program function to find the max of three numbers using a function to find largest of two numbers.

a=input("Enter the first number :")
b=input("Enter the second number :")
c=input("Enter the third number :")

def maxof2(x,y):
	if x > y:
		return x
	else:
		return y
def maxof3(x,y):
	if x > y:
		return x
	else:
		return y

print "The max of",a,b,c,"is :", maxof3(maxof2(a,b),c)

