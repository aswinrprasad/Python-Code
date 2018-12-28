import calc as op 

def trig(cal,j):
	op1=''
	while cal[j]>='a' and cal[j] <= 'z' or cal[j]>='A' and cal[j] <= 'Z':
		op1+=cal[j]
		j+=1
	if op1=='Sin' or op1=='sin' or op1=='Cos' or op1=='cos' or op1=='Tan' or op1=='tan' or op1=='cosec' or op1=='Cosec' or op1=='Sec' or op1=='sec' or op1=='Cot' or op1=='cot':
		print op1
		return op1
	else :
		print "Invalid!! Try again!!"
		exit(0)

while(True):
	print "MENU of available calculations :\n1.Add(+)\n2.Subtract(-)\n3.Divivde(/)\n4.Multiply(*)\n5.Remainder(%)\n6.Power(^)\nType Exit/exit to quit the program :\n\n",

	ch=raw_input("Enter a calculation(eg: 4+3) to be done : ")
	if ch == 'Exit' or ch== 'exit':
		exit(0)
	n1=''
	n2=''
	for i in range(len(ch)):
		#if i == ' ' or i>='a' and i<='z' or i>='A' and i <='Z':
		# ch[0]>='a' and ch[0] <= 'z' or ch[0]>='A' and ch[0] <= 'Z' or
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
				trigop=trig(ch,opf)
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
		print op.add2(int(n1),int(n2))
	elif ch[opf]=='-' :
		print "\n",n1+ch[opf]+n2,"=",
		print op.sub2(int(n1),int(n2))
	elif ch[opf]=='/' :
		print "\n",n1+ch[opf]+n2,"=",
		print op.div2(int(n1),int(n2))
	elif ch[opf]=='*' :	
		print "\n",n1+ch[opf]+n2,"=",
		print op.mul2(int(n1),int(n2))
	elif ch[opf]=='%' :
		print "\n",n1+ch[opf]+n2,"=",
		print op.rem1(int(n1),int(n2))
	elif ch[opf]=='^' :	
		print "\n",n1+ch[opf]+n2,"=",
		print op.pow(int(n1),int(n2))
	elif trigop == 'Sin' or trigop == 'sin':
		print "\n",n1+trigop+n2,"=",
		print op.sinc(int(n1),int(n2))
	elif trigop == 'Cos' or trigop == 'cos':
		print "\n",n1+trigop+n2,"=",
		print op.cosc(int(n1),int(n2))
	elif trigop == 'Tan' or trigop == 'tan':
		print "\n",n1+trigop+n2,"=",
		print op.tanc(int(n1),int(n2))
	elif trigop == 'Cosec' or trigop == 'cosec':
		print "\n",n1+trigop+n2,"=",
		print op.cosecc(int(n1),int(n2))
	elif trigop == 'Sec' or trigop == 'sec':
		print "\n",n1+trigop+n2,"=",
		print op.secc(int(n1),int(n2))
	elif trigop == 'Cot' or trigop == 'cot':
		print "\n",n1+trigop+n2,"=",
		print op.cotc(int(n1),int(n2))
	else :	
		print "Invalid operator!!"

	print "\n\n"

