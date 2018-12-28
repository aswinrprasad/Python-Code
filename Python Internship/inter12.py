f=open("/home/aswinrprasad/Documents/Python/text.txt",'w')
f.write("Hello my name is Aswin I love my country")
f.close()
f=open("/home/aswinrprasad/Documents/Python/text.txt")
a=f.read()
f.close()
flag=0
print "File contents :\n",a
li=a.split(" ")

print "\nThe list now :\n",li

x=raw_input("\nEnter a word to search in file :")
for i in li:
	if i==x :
		flag=1
		break
if flag==1:
	print "The word is present in the file."
else:
	print "No word present."