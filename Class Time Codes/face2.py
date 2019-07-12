#Program to convert Binary values to decimal.

n=raw_input("Enter the binary number to convert to decimal :")
n=reversed(n)
j,dec=0,0
for i in n:
    dec+=int(i)*(2**j)
    j+=1

print "The decimal equivalent is :",dec