#HackerRank problem : Making Anagrams


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    li=list(a)
    li1=list(b)
    
    i=0
    n=len(li)
    m=len(li1)
    while i<n:
        j=0
        while j<m and i<n:
            if li[i]==li1[j]:
                del li[i]
                del li1[j]
                m=len(li1)
                n=len(li)
                if j-1>=-1:
                    j-=1
                if i-1 >=-1:
                    i-=1
            j+=1
        i+=1
        
    
    return len(li)+len(li1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
