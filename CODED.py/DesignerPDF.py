#Designer PDF Viewer - Hackerrank Question

h,word,a= map(int, raw_input().rstrip().split()),raw_input(),[chr(x) for x in xrange(97, 123)] 
print max([i for i in {k:v for k,v in zip(a,h)}.items() if i[0] in word] , key = lambda x:x[1])[1] * len(word)
