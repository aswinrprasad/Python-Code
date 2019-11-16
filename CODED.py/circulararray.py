#Circular Array Rotation - Hackerrank

def circularArrayRotation(a, k, queries):
    a=(a[-k:] + a[:-k]) 
    for i in queries:
        print a[i]


nkq = raw_input().split()
n,k,q = int(nkq[0]),int(nkq[1]),int(nkq[2])
a = map(int, raw_input().rstrip().split())
queries = []
for _ in xrange(q):
    queries_item = int(raw_input())
    queries.append(queries_item)
circularArrayRotation(a, k, queries)


