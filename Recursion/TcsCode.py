#Pn(x)=((2n-1)*x*Pn-1(x)-(n-1)Pn-2(x))/n
#The legendre polynomials
#This code returns the value of Pn(x)

def pol(x , n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return ((((2*n-1)*x*pol(x,n-1))-((n-1)*pol(x,n-2)))/n)

x=input()
n=input()

print round(pol(x,n),3)