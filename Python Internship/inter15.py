
def fact(n):
    if(n <= 1):
        return 1
    else:
        return(n*fact(n-1))

n=input("Enter a number to find factorial of :")
print "The factorial of",n,"is :",fact(n)

