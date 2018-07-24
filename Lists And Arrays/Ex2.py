#Program to print any Arithmetic progression and to append next n terms to the initial progression.

a=input("Enter first term in A.P :")
d=input("Enter common difference of A.P :")
size=input("Enter limit for values in A.P :")

li=range(a,size,d)
print "A.P is :",li

size1=input("\nEnter new limit of the A.P :")
li2=range(li[-1]+d,size1,d)

print "Next 4 terms of the A.P is :",li2

li+=li2

print "The A.P now is :",li
