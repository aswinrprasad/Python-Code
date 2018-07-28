#A high level maths students takes a test. Write a program where the student enters their
#percentage mark. The program outputs their grade according to:
#70% or more grade 7
#Between 60 and 69 grade 6
#Between 50 and 59 grade 5
#Between 40 and 49 grade 4
#Between 30 and 39 grade 3
#Between 20 and 29 grade 2
#Less than 20 a grade 1

mark=input("Enter marks in percentage :")
if 70 <= mark <= 100:
	print "Grade point: 7"
elif 60 <= mark < 70:
	print "Grade point: 6"
elif 50 <= mark < 60:
	print "Grade point: 5"
elif 40 <= mark < 50:
	print "Grade point: 4"
elif 30 <= mark < 40:
	print "Grade point: 3"
elif 20 <= mark < 10:
	print "Grade point: 2"
elif 0 <= mark < 20:
	print "Grade point: 1"
else:
	print "Invalid Input"
	
