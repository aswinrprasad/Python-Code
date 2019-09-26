import random as r
n=input("Enter size of prefix free code sequence :")

li=[]
li1=[]
dup=[]
for i in range(n):
	li.append(int(r.randrange(12)))
dup=li[:]
dup.sort()
while(len(li)>=2):
	li.sort()
	print li
	a=li[0]+li[1]
	li1.append(a)
	del li[0]
	del li[0]
	li.insert(0,a)

print li
print li1
print dup

