li=[2,4,6,8,10,12,14,16]
print "A.P is :",li

a=li[0]
d=li[1]-li[0]
last=li[7]

li2=[last+d,last+2*d,last+3*d,last+4*d]

print "Next 4 terms of the A.P is :",li2

li.append(li2[0])
li.append(li2[1])
li.append(li2[2])
li.append(li2[3])

print "The A.P now is :",li
