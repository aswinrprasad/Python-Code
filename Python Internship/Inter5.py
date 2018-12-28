limit=input("Enter how many values you want to print :")

a=0
b=1
print a,b,
'''
for i in range(limit-2):
	c=a+b
	a=b
	b=c
	print c,	
'''
i=0
while(i<limit-2):
	c=a+b
	a=b
	b=c
	print c,
	i+=1
