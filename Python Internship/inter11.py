f=open("/home/aswinrprasad/Documents/Python/text.txt",'w')
f.write("abAB542**/##L:'}+++")
f.close()
f=open("/home/aswinrprasad/Documents/Python/text.txt")
a=f.read()
f.close()
print a
for i in range(len(a)):
	if a[i] >= 'a' and a[i] <='z':
		f=open("/home/aswinrprasad/Documents/Python/lower.txt",'a')
		f.write(a[i])
		f.close()
	elif a[i]>='A' and a[i]<='Z':
		f=open("/home/aswinrprasad/Documents/Python/upper.txt",'a')
		f.write(a[i])
		f.close()
	elif a[i]>='0' and a[i]<='9':
		f=open("/home/aswinrprasad/Documents/Python/digit.txt",'a')
		f.write(a[i])
		f.close()
	else:
		f=open("/home/aswinrprasad/Documents/Python/special.txt",'a')
		f.write(a[i])
		f.close()