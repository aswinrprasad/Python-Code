#Migratory Birds - Hackerrank Problem

n,arr=input(),map(int, raw_input().split())
unique,d=set(arr),{}
print max({i:arr.count(i) for i in unique}.items(),key= lambda x:x[1])[0]
