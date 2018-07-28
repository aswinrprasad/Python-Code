#Create a list that contains the first 3 terms of an arithmetic series.Then increase the list to include the next 4 terms of the arithmetic series. You don’t need to use a loop.

li=[3,6,9]
print "The A.P is",li

a=li[0]
d=li[1]-li[0]
last=li[2]

li+=range(last+d,last+5*d,d)
print "The A.P now with next 4 terms is :",li
