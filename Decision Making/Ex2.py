#The rules for winning the prize have got stricter. The first name must now have more than 5
#characters (as well as end in the letter a). Modify the program in Exercise 1.

name=raw_input("Enter your first name :")
size=len(name)
if size >= 5:
	if name[size-1] == 'a':
		print "Congrats!! Your name ends with the letter A and have 5 characters. You won $1000."
	else:
		print "Name has 5 characters but does not end with letter A. Better luck next time."
else:
	print "Your name doesn't end with A or have 5 characters. Better luck next time."

