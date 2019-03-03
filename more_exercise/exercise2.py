students_number=int(input("Enter number of Students :"))
per_student_kharcha=int(input("Enter per student expense :"))
total_kharcha=students_number*per_student_kharcha
if total_kharcha<50000:
	print ("Ham kharche ke andar hai ")
else:
	print ("kharche se bahar hai ")