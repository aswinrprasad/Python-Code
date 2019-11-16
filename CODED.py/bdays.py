#Beautiful days - hackerrank

def beautifulDays(i, j, k):
    cnt=0
    for d in range(i,j+1):
        dr = int(str(d)[::-1])
        if (d-dr < 0) and ((d-dr)*-1)%k==0 :
            cnt+=1
        elif (d-dr)%k==0 :
            cnt+=1
    return cnt

ijk = map(int,raw_input().split())
print beautifulDays(ijk[0],ijk[1],ijk[2])
