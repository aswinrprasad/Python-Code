mark=input("Enter mark out of 100 :")

if mark >=0 and mark <= 35:
	print "FAIL!"
elif mark >35 and mark <=50:
	print "Grade : D"
elif mark >50 and mark <=60:
	print "Grade : C"
elif mark >60 and mark <=70:
	print "Grade : B"
elif mark >70 and mark <=80:
	print "Grade : B+"
elif mark >80 and mark <=90:
	print "Grade : A"
elif mark >90 and mark <=100:
	print "Grade : A+"
else:
	print "Invalid entry"


