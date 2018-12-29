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
	return a*m.tan(m.radians(b))

def cosecc(a,b):
	return a*(1/m.sin(m.radians(b)))

def secc(a,b):
	return a*(1/m.cos(m.radians(b)))

def cotc(a,b):
	return a*(1/m.tan(m.radians(b)))