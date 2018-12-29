import math as m

def add2(a,b):
	return a+b

def sub2(a,b):
	return a-b

def div2(a,b):
	return a/b

def mul2(a,b):
	return a*b

def rem1(a,b):
	return a%b

def pow(a,b):
	return a**b

def sinc(a,b):
	n=(b-0)%180
	if n==0:
		return 0
	else:
		return a*m.sin(m.radians(b))

def cosc(a,b):
	n=(b-90)%180
	if n==0:
		return 0
	else:
		return a*m.cos(m.radians(b))

def tanc(a,b):
	if cosc(1,b) != 0: 
		return a*(sinc(a,b)/cosc(a,b))
	else:
		return "Not Defined!"

def cosecc(a,b):
	if m.sin(m.radians(b)) != 0: 
		return a*(1/m.sin(m.radians(b)))
	else:
		return "Not Defined!"	
def secc(a,b):
	if cosc(1,b) != 0: 
		return a*(1/m.cos(m.radians(b)))
	else:
		return "Not Defined!"

def cotc(a,b):
	if sinc(1,b) != 0: 
		return a*(cosc(a,b)/sinc(a,b))
	else:
		return "Not Defined!"

def logc(a,b):
	if b <= 0:
		return "Not defined!"
	else:
		return a*m.log10(b)

def expc(a,b):
		return a*m.exp(b)