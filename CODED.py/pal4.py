def checkPal(s1):
    cnt=0
    if s1==s1[::-1]:
        return 0
    else:
        while len(s1)!=0 :
            s1=s1[:-1]
            print s1
            cnt+=1
            if s1==s1[::-1]:
                return cnt  
        

t = input()
for i in xrange(t):
    print checkPal(raw_input())
