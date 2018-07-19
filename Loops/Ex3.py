limit=input("Enter how many times you want to print the statement :")
count=1
print "The statement is being printed by while loop.." 
while count <= limit :
	print "Tell me why I don't like mondays?"
	count+=1
print "The statement is being printed by for loop.."
for count in range(0,limit):
	print "Tell me why I don't like mondays?"
