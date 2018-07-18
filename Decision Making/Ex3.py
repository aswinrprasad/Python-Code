age=int(raw_input("Enter your age :"))
if 18 <= age < 65:
	print "Normal fare."
elif 0 < age < 18:
	print "Child Fare as you're younger than 18."
elif age >=65:
	print "You'll get pensioners discount as you're older than 65 ."
else:
	print "Not a valid age."
	exit()
	  
	
