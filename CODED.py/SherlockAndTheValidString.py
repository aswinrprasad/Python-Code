#Sherlock and the Valid String - Hackerrank 

def prod(d) : 
    p=1
    for i in d :
        if d[i]!=0: 
            p =p * d[i]
    return p

s = raw_input()

dic = {}
for i in s : 
    if i in dic.keys():
        continue
    else: 
        dic[i]= s.count(i)

if dic[dic.keys()[0]]**len(dic) != prod(dic) : 
    val= dic[dic.keys()[0]]
    for i in dic : 
        if val == dic[i] :
            f=True
        elif val == dic[i]-1 :
            f=True
        elif dic[i]-1 ==0 :
            if dic[dic.keys()[0]]**(len(dic)-1) != prod(dic) : 
                print "NO"
                exit(0)
            else:
                print "YES"
                exit(0)
        else :
            f=False
            break
    if f==True : 
        print "YES"
    else :
        print "NO"
else:
    print "YES"