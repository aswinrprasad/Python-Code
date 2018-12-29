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
	return a*m.sin(m.radians(b))

def cosc(a,b):
	return a*m.cos(m.radians(b))

def tanc(a,b):
	if m.cos(m.radians(b)) != 0: 
		return a*(m.tan(m.radians(b)))
	else:
		return "Not Defined!"

def cosecc(a,b):
	if m.sin(m.radians(b)) != 0: 
		return a*(1/m.sin(m.radians(b)))
	else:
		return "Not Defined!"	
def secc(a,b):
	if m.cos(m.radians(b)) != 0: 
		return a*(1/m.cos(m.radians(b)))
	elif m.cos(m.radians(b)) == float("inf"):
		return "Not Defined!"

def cotc(a,b):
	if m.tan(m.radians(b)) != 0: 
		return a*(1/m.tan(m.radians(b)))
	else:
		return "Not Defined!"