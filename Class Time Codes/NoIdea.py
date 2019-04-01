#No Idea (Hackerrank question)
li=[]
li+=raw_input().split()
n=int(li[0])
m=int(li[1])

li=[]
li+=map(int,raw_input().split())

A=[]
A+=map(int,raw_input().split())
A=set(A)

B=[]
B+=map(int,raw_input().split())
B=set(B)

sumx=0

for i in li:
    if i in A:
        sumx+=1
    elif i in B:
        sumx-=1
    else:
        k=0

print sumx