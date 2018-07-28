#Write a program where the user enters their full name, and a letter. The program counts the number of times the chosen letter is in the name.

name=raw_input("Enter your name :")
size=len(name)
check=raw_input("Enter a character to check if it is in your name :")
count=name.count(check)
print "The character ",check," is present ",count," times in the string." 
