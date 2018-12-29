import calc as op 

def word(cal,j):
	op1=''
	while cal[j]>='a' and cal[j] <= 'z' or cal[j]>='A' and cal[j] <= 'Z':
		op1+=cal[j]
		j+=1
	if op1=='Sin' or op1=='sin' or op1=='Cos' or op1=='cos' or op1=='Tan' or op1=='tan' or op1=='cosec' or op1=='Cosec' or op1=='Sec' or op1=='sec' or op1=='Cot' or op1=='cot':
		return op1
	else :
		print "Invalid!! Try again!!"
		exit(0)


print """\n\n\t\t******** PYCAL v0.3
		\t-Made By ASWIN RAGHUPRASAD ********\n\n"""


while(True):
	print "MENU of available calculations :\n1.Add(+)\n2.Subtract(-)\n3.Divivde(/)\n4.Multiply(*)\n5.Remainder(%)\n6.Power(^)\n7.Trigonometric functions(eg:aSin(b))\nType Exit/exit to quit the program :\n\n",

	ch=raw_input("Enter a calculation(eg: 4+3) to be done : ")
	if ch == 'Exit' or ch== 'exit':
		exit(0)

	n1=''
	n2=''

	if ch[0]==' ' or ch[-1]>='a' and ch[-1] <= 'z' or ch[-1]>='A' and ch[-1] <= 'Z':
		print "Invalid structure of input. Try again!"
		exit(0)

	i=0 
	while(i<len(ch)):
		if ch[i]>='0' and ch[i]<='9':
			n1+=ch[i]
		else:
			opf=i
			if ch[opf] >='a' and ch[opf] <= 'z' or ch[opf]>='A' and ch[opf] <= 'Z':
				trigop=word(ch,opf)
				if n1=='':
					n1='1'
			elif ch[opf] == ' ':
				print "Invalid operand! Try again!"
				exit(0)
			break
		i+=1


	while(i<len(ch)):
		if ch[i]>='0' and ch[i]<='9':
			n2+=ch[i]
		i+=1


	if ch[opf]=='+' :
		print "\n",n1+ch[opf]+n2,"=",
		print op.add2(float(n1),float(n2))
	elif ch[opf]=='-' :
		print "\n",n1+ch[opf]+n2,"=",
		print op.sub2(float(n1),float(n2))
	elif ch[opf]=='/' :
		print "\n",n1+ch[opf]+n2,"=",
		print op.div2(float(n1),float(n2))
	elif ch[opf]=='*' :	
		print "\n",n1+ch[opf]+n2,"=",
		print op.mul2(float(n1),float(n2))
	elif ch[opf]=='%' :
		print "\n",n1+ch[opf]+n2,"=",
		print op.rem1(float(n1),float(n2))
	elif ch[opf]=='^' :	
		print "\n",n1+ch[opf]+n2,"=",
		print op.pow(float(n1),float(n2))
	elif trigop == 'Sin' or trigop == 'sin':
		print "\n",n1+trigop+n2,"=",
		print op.sinc(float(n1),float(n2))
	elif trigop == 'Cos' or trigop == 'cos':
		print "\n",n1+trigop+n2,"=",
		print op.cosc(float(n1),float(n2))
	elif trigop == 'Tan' or trigop == 'tan':
		print "\n",n1+trigop+n2,"=",
		print op.tanc(float(n1),float(n2))
	elif trigop == 'Cosec' or trigop == 'cosec':
		print "\n",n1+trigop+n2,"=",
		print op.cosecc(float(n1),float(n2))
	elif trigop == 'Sec' or trigop == 'sec':
		print "\n",n1+trigop+n2,"=",
		print op.secc(float(n1),float(n2))
	elif trigop == 'Cot' or trigop == 'cot':
		print "\n",n1+trigop+n2,"=",
		print op.cotc(float(n1),float(n2))
	else :	
		print "Invalid operator!!"

	
	print "\n\n"

