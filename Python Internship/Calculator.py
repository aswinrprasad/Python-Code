import calc as op 

while(True):
	print "MENU of available calculations :\n1.Add\n2.Subtract\n3.Divivde\n4.Multiply\n5.Remainder\n6.Power\nType Exit/exit to quit the program :\n",

	ch=raw_input("Enter a calculation(eg: 4+3) to be done : ")
	if ch == 'Exit' or ch== 'exit':
		exit(0)
	n1=''
	n2=''
	for i in ch:
		if i == ' ':
			print "Invalid structure of input. Please don't include spacetab!"
			exit(0)
	i=0 
	while(i<len(ch)):
		if ch[i]>='0' and ch[i]<='9':
			n1+=ch[i]
			opf=i
		else:
			if ch[i]>='0' and ch[i]<='9':
				n2+=ch[i]
		i+=1

	opf=opf+1
	print "\n",n1+ch[opf]+n2,"=",
	if ch[opf]=='+' :
		print op.add2(int(n1),int(n2))
	elif ch[opf]=='-' :
		print op.sub2(int(n1),int(n2))
	elif ch[opf]=='/' :
		print op.div2(int(n1),int(n2))
	elif ch[opf]=='*' :	
		print op.mul2(int(n1),int(n2))
	elif ch[opf]=='%' :
		print op.rem1(int(n1),int(n2))
	elif ch[opf]=='^' :	
		print op.pow(int(n1),int(n2))
	else :	
		print "Invalid operator!!"

	print "\n\n"

