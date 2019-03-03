a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
def cal(a,b,operation):
	if operation=="add":
		print (a+b)
	if operation=="subtract":
		print (a-b)
	if operation=="multiply":
		print (a*b)
	if operation=="devide":
		print (a//b)
	if operation=="modulus":
		print (a%b)
cal(a,b,"add")
cal(a,b, "subtract")
cal(a,b,"multiply")
cal(a,b,"devide")
cal(a,b,"modulus")