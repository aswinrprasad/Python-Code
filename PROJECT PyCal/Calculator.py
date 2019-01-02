import calc as op 

def word(cal,j):
	op1=''
	while cal[j]>='a' and cal[j] <= 'z' or cal[j]>='A' and cal[j] <= 'Z':
		op1+=cal[j]
		j+=1
	if 'Ans' in op1:
		return op1,j
	if op1=='Sin' or op1=='sin' or op1=='Cos' or op1=='cos' or op1=='Tan' or op1=='tan' or op1=='cosec' or op1=='Cosec' or op1=='Sec' or op1=='sec' or op1=='Cot' or op1=='cot' or op1=='log' or op1 == 'e' or op1 == 'p' or op1== 'c':
		return op1,j
	else :
		print op1,j
		print "Invalid!! Try again!!"
		exit(0)

def Answer(n1,ch,opa):
	i=0
	while i<len(ch):
		if ch[i]>='0' and ch[i]<='9' or ch[i]=='.' or ch[i]== '-' or ch[i] >='a' and ch[i] <= 'z' or ch[i]>='A' and ch[i] <= 'Z':
			k=0
		else:
			opa=i
			if ch[opa] == ' ':	
				print "Invalid operand! Try again!"
				exit(0)
			break
		i+=1
	n2=''
	while(i<len(ch)):
		if ch[i]>='0' and ch[i]<='9' or ch[i]=='.' or ch[i]== '-':
			n2+=ch[i]
		i+=1
	return opa,str(n2)


print """\n\n\t\t******** PYCAL v0.7\t
		\t-Made By ASWIN RAGHUPRASAD ********\t\n\n"""
print """\tNOTE:It is a binary calculator which accepts two inputs and an operator.\t\n\n"""


while(True):
	print "MENU of available calculations :\n1.Add(+)\n2.Subtract(-)\n3.Divivde(/)\n4.Multiply(*)\n5.Remainder(%)\n6.Power(^)\n7.Trigonometric functions(eg:aSin(b))\n8.Log(eg:alogb)\n9.Exponential(eg:ae(b))\n10.Factorial(eg:5!)\n11.Permutation(eg:4p2)\n12.Combinations(eg:4c2)\nPs:Previous results can be used.(eg:Ans+3)\nType Exit/exit to quit the program :\n\n",

	ch=raw_input("Enter a calculation(eg: 4+3) to be done : ")
	if ch == 'Exit' or ch== 'exit':
		exit(0)

	n1=''
	n2=''
	trigop=''
	if ch[0]==' ' or ch[-1]>='a' and ch[-1] <= 'z' or ch[-1]>='A' and ch[-1] <= 'Z':
		print "Invalid structure of input. Try again!"
		exit(0)

	i=0 
	while(i<len(ch)):
		if ch[i]>='0' and ch[i]<='9' or ch[i]=='.' or ch[i]== '-':
			n1+=ch[i]
		else:
			opf=i
			if ch[opf] >='a' and ch[opf] <= 'z' or ch[opf]>='A' and ch[opf] <= 'Z':
				trigop,j=word(ch,opf)
				if n1=='':
					n1='1'
			elif ch[opf] == ' ':
				print "Invalid operand! Try again!"
				exit(0)
			break
		i+=1


	while(i<len(ch)):
		if ch[i]>='0' and ch[i]<='9' or ch[i]=='.' or ch[i]== '-':
			n2+=ch[i]
		i+=1


	if trigop[0:3] =='Ans':
		try:
			opa=0
			if isinstance(Ans,str)!=True:
				n1=str(Ans)
			else:
				print "The previous result is not defined.Do another calculation without 'Ans' this time.\n\n"
				continue
			opf,n2=Answer(n1,ch,opa)
			if trigop!='Ans':
				opf=3
				if ch[opf] >='a' and ch[opf] <= 'z' or ch[opf]>='A' and ch[opf] <= 'Z':
					trigop,j=word(ch,opf)
					while(j<len(ch)):
						if ch[j]>='0' and ch[j]<='9' or ch[j]=='.' or ch[j]== '-':
							n2+=ch[j]
						j+=1
		except NameError:
			print "You have not done any calculations yet for previous result to be stored! Try again!\n\n"
			continue

	if ch[opf]=='+' :
		Ans=op.add2(float(n1),float(n2))
		print "\n",n1+ch[opf]+n2,"=",Ans
	elif ch[opf]=='-' :
		Ans=op.sub2(float(n1),float(n2))
		print "\n",n1+ch[opf]+n2,"=",Ans
	elif ch[opf]=='/' :
		Ans=op.div2(float(n1),float(n2))
		print "\n",n1+ch[opf]+n2,"=",Ans
	elif ch[opf]=='*' :	
		Ans=op.mul2(float(n1),float(n2))
		print "\n",n1+ch[opf]+n2,"=",Ans
	elif ch[opf]=='%' :
		Ans=op.rem1(float(n1),float(n2))
		print "\n",n1+ch[opf]+n2,"=",Ans
	elif ch[opf]=='^' :	
		Ans=op.pow(float(n1),float(n2))
		print "\n",n1+ch[opf]+n2,"=",Ans
	elif trigop == 'Sin' or trigop == 'sin':
		Ans=op.sinc(float(n1),float(n2))
		print "\n",n1+trigop+n2,"=",Ans
	elif trigop == 'Cos' or trigop == 'cos':
		Ans=op.cosc(float(n1),float(n2))
		print "\n",n1+trigop+n2,"=",Ans
	elif trigop == 'Tan' or trigop == 'tan':
		Ans=op.tanc(float(n1),float(n2))
		print "\n",n1+trigop+n2,"=",Ans
	elif trigop == 'Cosec' or trigop == 'cosec':
		Ans=op.cosecc(float(n1),float(n2))
		print "\n",n1+trigop+n2,"=",Ans
	elif trigop == 'Sec' or trigop == 'sec':
		Ans=op.secc(float(n1),float(n2))
		print "\n",n1+trigop+n2,"=",Ans
	elif trigop == 'Cot' or trigop == 'cot':
		Ans=op.cotc(float(n1),float(n2))
		print "\n",n1+trigop+n2,"=",Ans
	elif trigop == 'log':
		Ans=op.logc(float(n1),float(n2))
		print "\n",n1+trigop+n2,'=',Ans
	elif trigop == 'e':
		print "\n",n1+trigop+"("+n2+")",'=',op.expc(float(n1),float(n2))
	elif ch[opf] == '!':
		try:
			if (float(n1)).is_integer() == True:
				n1=float(n1)
				n1=int(n1)
			if op.fact(int(n1)) == None:
				print "Cannot find factorial of a negative number.Try again!\n\n"
				continue
			Ans=op.fact(int(n1))
			print "\n",str(n1)+ch[opf],"=",Ans
		except ValueError:
			print "Input cannot be a decimal value for factorial calculation!! Try again!"
	elif trigop == 'p':
		try:
			if (float(n1)).is_integer() == True:
				n1=float(n1)
				n1=int(n1)
			if (float(n2)).is_integer() == True:
				n2=float(n2)
				n2=int(n2)
			if op.fact(int(n1)) == None or op.fact(int(n2)) == None:
				print "Cannot find factorial of a negative number.Try again!\n\n"
				continue
			Ans=op.perm(int(n1),int(n2))
			print "\n",str(n1)+trigop+str(n2),"=",Ans
		except ValueError:
			print "Input cannot be a decimal value for factorial calculation!! Try again!"
	elif trigop == 'c':
		try:
			if (float(n1)).is_integer() == True:
				n1=float(n1)
				n1=int(n1)
			if (float(n2)).is_integer() == True:
				n2=float(n2)
				n2=int(n2)
			if op.fact(int(n1)) == None or op.fact(int(n2)) == None:
				print "Cannot find factorial of a negative number.Try again!\n\n"
				continue
			Ans=op.comb(int(n1),int(n2))
			print "\n",str(n1)+trigop+str(n2),"=",Ans
		except ValueError:
			print "Input cannot be a decimal value for factorial calculation!! Try again!"
	else :	
		print "Invalid operator!!"

	
	print "\n\n"

