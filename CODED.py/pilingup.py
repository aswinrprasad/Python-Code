#A code for the problem 'Piling Up!' in hackerrank.

t=input()
for i in range(t):
    n=input()
    li=map(int,raw_input().split())
    k=len(li)
    stack=[]
    while k!=0:
        sideleft=li[0]
        sideright=li[-1]
        if sideleft >= sideright:
            stack.append(sideleft)
        else:
            stack.append(sideright)

        del li[0]
        if len(li)!=0:
            del li[-1]
        k=len(li)
        
    
    if sorted(stack, reverse=True) == stack:
        print "Yes"
    else:
        print "No"

