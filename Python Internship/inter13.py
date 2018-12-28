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

longest_word = ''
for word in li:
    if len(word) > len(longest_word):
        longest_word = word
print "\nThe largest word is :",longest_word
