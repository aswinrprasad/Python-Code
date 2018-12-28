x=input("Enter a number :")
j=x
y=0

while j != 0:
	y+= j%10
	y*=10
	j/=10

if y/10 == x:
	print "Palindrome"
else :
	print "Not palindrome."


