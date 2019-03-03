student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87,9]
i=0
less=0
more=0
while i<len(student_marks):
	if student_marks[i]<50:
		less=less+1
	else:
		more=more+1
	i=i+1
print ("more 50: ", more)
print ("less 50: ", less)