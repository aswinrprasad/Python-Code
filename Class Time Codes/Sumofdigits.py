#Program to find the sum of digits of n numbers.

t=input("Enter no.of test  cases :")
li=[]

if t>=1 and t<=30 :
	print "Enter values :"
	for i in range(0,t) :
		obj=int(input())
	        li.append(obj)

for i in range(0,t):
	sum1=0
	dup=li[i]
    	while li[i] > 0:
        	val=li[i]%10
        	sum1+=int(val)
        	li[i]/=10
    	print "The sum of",dup,"is :",sum1
    
