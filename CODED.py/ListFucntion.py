#Pogram to print sum and product of all elements in a list using functions

def sum1(li):
	sumx=0
	for i in range(0,len(li)):
		sumx+=li[i]
	return sumx

def mult1(li):
	mult=1
	for i in range(0,len(li)):
		mult*=li[i]
	return mult

t=input("Enter the size of the list :")
li=[]
print "Enter values of the list :"
for i in range(0,t) :
	obj=int(input())
        li.append(obj)
print "The list is :",li
print "The sum of the elements of the list is :",sum1(li)
print "The product of the elements of the list is :",mult1(li)
