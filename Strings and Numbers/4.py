#You are writing a program that process the details of new students entering a high school. The user inputs, the name, their date of birth, the last 4 digits of their personal number. The program outputs: the name and personal number as a single string, and also the age of the student. Depending on how you have wrote the program you might need to use str(number) In this context can you work what str(number) does?

name=raw_input("Enter the name of the student :")
date = raw_input("Enter the date in DOB : ")
month = raw_input("Enter the month in DOB : ")
year = raw_input("Enter the year in DOB : ")
lastdigit=raw_input("Enter the last 4 digits of your phone number : ")
age=raw_input("Enter the age of the student : ")

dob=date+" "+month+" "+year
x=name+lastdigit

print "Id of the student is :",x," and age is : ",age
