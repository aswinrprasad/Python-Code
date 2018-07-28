#A program where the person enters their first name. The program determines the
#length of the name, and then determines if the name ends with the letter “a”. If the name
#ends with an a, then the person wins a 1000 dollar prize. The program informs the person
#that they have or have not won the prize.

name=raw_input("Enter your first name :")
size=len(name)
if name[size-1] == 'a':
	print "Congrats!! Your name ends with the letter A. You won $1000."
else:
	print "Your name doesn't end with A. Better luck next time."
