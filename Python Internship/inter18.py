import calc as op 

while(True):
	print "MENU \n1.Add\n2.Subtract\n3.Divivde\n4.Multiply\n5.Remainder\n6.Power\n7.Exit\n\nEnter your choice for calculation :",

	ch=input()
	if ch == 7:
		exit(0)
	
	a=input("Enter first input :")
	b=input("Enter second input :")
	if ch==1 :
		print "The sum is :",op.add2(a,b)
	elif ch==2 :
		print "The difference is :",op.sub2(a,b)
	elif ch==3 :
		print "The division result is :",op.div2(a,b)
	elif ch==4 :	
		print "The product is :",op.mul2(a,b)
	elif ch==5 :
		print "The remainder is :",op.rem1(a,b)
	elif ch== 6 :	
		print "The result of a^b is :",op.pow(a,b)
	else :	
		print "Invalid choice!!"

	print "\n\n"


