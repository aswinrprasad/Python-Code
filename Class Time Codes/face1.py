"""
7+7*0=7
7+7*2=21
21+7*4=49
49+7*6=91
"""
print "The series : 7 21 49 91 147 217 301 399 ..."
n=input("Enter the nth term in the series to display :")
li=[7]

j=0
i=0
while j<n:
    li.append(li[j]+7*i)
    j+=1
    i+=2

del li[0]
print "The n'th term in the series is :",li[n-1] 
