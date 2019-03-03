x=int(raw_input("Enter a number "))
y=list(str(x))
s=0
for i in range(len(y)):
	s=s+int(y[i])
if x%s==0:
	print x,"harshad number hai"
else:
	print x,"harshad number nahi hai"