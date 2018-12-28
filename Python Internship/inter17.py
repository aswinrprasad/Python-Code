class billing:
	totamnt=0
	def __init__(self,iname,price,qty):
		self.iname=iname
		self.price=price
		self.qty=qty
		self.subtotal=0
	def display(self):
		self.subtotal=self.qty * self.price
		print self.iname,"\t",self.qty,"\t\t",self.price,"\t\t",self.subtotal
		billing.totamnt+=self.subtotal

b={}
noofitems=input("Enter how many items purchased :")
for i in range(noofitems):
	n=raw_input("Enter item name :")
	p=input("Price :")
	q=input("Quantity :")
	b[i]=billing(n,p,q)

print "\nItem\tPrice\t    Quantity\tPrice\Subtotal"
for i in range(noofitems):
	b[i].display()
	print "\n"

print "The total amount is :",billing.totamnt
