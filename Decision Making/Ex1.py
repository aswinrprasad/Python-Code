name=raw_input("Enter your first name :")
size=len(name)
if name[size-1] == 'a':
	print "Congrats!! Your name ends with the letter A. You won $1000."
else:
	print "Your name doesn't end with A. Better luck next time."
