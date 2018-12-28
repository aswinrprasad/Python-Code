x=input("Enter a number :")
j=x
sumx=0
while j!=0:
	sumx+= j%10
	j/=10

print "The sum is :",sumx