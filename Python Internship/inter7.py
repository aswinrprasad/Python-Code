x=input("Enter a number :")
i=x
j=x
power=0
sumx=0

while i!=0 :
	i/=10
	power+=1

while j!=0:
	sumx+= (j%10)**power
	j/=10

if sumx == x :
	print "It is an amstrong number."
else : 
	print "It is not an amstrong number." 
