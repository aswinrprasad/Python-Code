#DICTIONARIES IN PYTHON

fruits=['apple','pear','orange','pinapple']
nbrFruits=[10,6,8,1]
fruitDict={}
for index,fruit in enumerate(fruits):
	fruitDict[fruit]=nbrFruits[index]
print fruitDict

#Write code to find how many apples are present in the store.
print "No of apples in the store is :",fruitDict['apple']

#Write code to update dictionary when k oranges are sold.
k=input("Enter no.of oranges sold :")
fruitDict['orange']-=k
if k>8 :
	print "Invalid input"	
	exit()
print "The no.of oranges left after",k," oranges are sold :",fruitDict['orange']
