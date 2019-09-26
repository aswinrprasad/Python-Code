#Program to check if there is at least one element common in two lists using set property and functions to implement it.

def Overlapping(size1,size2):
	print "Enter elements of list 1:"
	for i in range(0,size1):
		obj=int(input())
		li1.append(obj)
	print "Enter elements of list 2:"
	for i in range(0,size2):
		obj=int(input())
		li2.append(obj)
	
	return is_member(li1,li2)

def is_member(li1,li2):
	s1=set(li1)
	s2=set(li2)
	if s1 & s2 :
		return True
	else:
		return False

t1=input("Enter the size of list 1:")
t2=input("Enter the size of list 2:")
li1=[]
li2=[]
x=Overlapping(t1,t2)
if x==True :
	print "There is at least one same element in the given lists."
else :
	print "No same elements in the given lists."
	
	
