#Write a Python program to print the words, if two words from a list of words starting with letter 'P'

import re

size=input("Enter list size :") 
l = []
print "Enter strings for the list :",
for i in range(0,size) :
	word=raw_input()	
	l.append(word)

print "The list here is :",l

print "The list element that matches given pattern is : ",
for w in l:
        pat = re.match("(P\w+)\W(P\w+)", w)
        if pat:
            print list(pat.groups()),
