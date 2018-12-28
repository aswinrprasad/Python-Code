def add2(a,b):
	return a+b

def sub2(a,b):
	return a-b

def div2(a,b):
	return a/b

def mul2(a,b):
	return a*b

def rem1(a,b):
	return a%b

def pow(a,b):
	return a**b

while(True):
	print "MENU \n1.Add\n2.Subtract\n3.Divivde\n4.Multiply\n5.Remainder\n6.Power\n7.Exit\n\nEnter your choice for calculation :",

	ch=input()
	if ch == 7:
		exit(0)
	
	a=input("Enter first input :")
	b=input("Enter second input :")
	if ch==1 :
		print "The sum is :",add2(a,b)
	elif ch==2 :
		print "The difference is :",sub2(a,b)
	elif ch==3 :
		print "The division result is :",div2(a,b)
	elif ch==4 :	
		print "The product is :",mul2(a,b)
	elif ch==5 :
		print "The remainder is :",rem1(a,b)
	elif ch== 6 :	
		print "The result of a^b is :",pow(a,b)
	else :	
		print "Invalid choice!!"

	print "\n\n"


