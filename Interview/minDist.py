#Program to print k number of points in a list(in the order of increasing distances) which are closest to a given vertex of form (x,y) using distnce formula.

import math as m

d={}
def nearestPoints(points,vertex):
    global d
    for i in points:
        d[tuple(i)]= m.sqrt((vertex[0]-i[0])**2 + (vertex[1]-i[1])**2)
    return sorted(d.items(), key=lambda x : x[1])

points=[[1,2],[2,3],[1,-1],[4,3]]
vertex=[4,2]

k=2
if k<0:
    raise ValueError("Number of points to return cannot be empty")
print "The nearest points are :",
for i in xrange(k):
    print nearestPoints(points,vertex)[i][0],
    
    
    


