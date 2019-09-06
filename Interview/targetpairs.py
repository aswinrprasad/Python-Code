#A program to print the first pair in a list that sums up to a target value with O(n) time complexity

def pairs(li,target):
    for i in xrange(len(li)):
            if target-li[i] in li[i+1:]:
                    return str(li[i])+" and "+str(target-li[i])
    return "not present in the list!"

li=map(int,raw_input("Enter list elements :").split())
target=input("Enter target element :")

print "The pair of elements that sum upto the target element is ",pairs(li,target)
