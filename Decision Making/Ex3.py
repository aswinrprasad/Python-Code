#Write a program where a person enter the year of their birth. Person below the age of 18
#have to buy a child fare, and persons 65 and above get a pensioners discount. Your program
#will calculate their age and advise them on the right ticket according to their age.

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
	  
	
