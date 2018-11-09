x=str(raw_input("Enter String input :"))
arr=[]

for t in range(0,10):
	arr.append(int(0))


for no in range(0,10):
	cnt=0
	for i in range(0, len(x)):
		d=str(no)
		if x[i]==d :
			cnt+=1
			arr[no]=cnt

for t in range(0,10):
	print "The number of %d's in the sting is :"% t,arr[t]

