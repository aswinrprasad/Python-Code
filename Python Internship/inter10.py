x=raw_input("Enter a sring :")

l=len(x)
n=-1
str1=''
for i in range(l):
	str1=str1 + x[n]
	n-=1

if str1 == x :
	print "String is a palindrome."
else:
	print "Not palindrome."
