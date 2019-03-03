# part 1
number_x=20
number_y=30
def calculator(number_x,number_y,operation):
	if operation=="add":
		add_result=(number_x + number_y)
		return (add_result)
	if operation=="multiply":
		multiply_result=(number_x * number_y)
		return (multiply_result)
	if operation=="subtract":
		subtract_result=(number_x - number_y)
		return (subtract_result)
	if operation=="devide":
		devide_result=(number_x // number_y)
		return (devide_result)
	if operation=="modulus":
		mod_result=(number_x % number_y)
		return (number6)
# part 2
 
calculator(number_x,number_y, "add")
calculator(number_x,number_y, "multiply")
calculator(number_x,number_y, "devide")
calculator(number_x,number_y, "subtract")
# # part 3
# third part tab chalta h jab baki ke do part ko comment kar do ise me theek karuga 
def list_change(a,b):
	i=0
	if len(a)==len(b):
		while i<len(a):
			multiply_result=(a[i]*b[i])
			print (multiply_result)
			i=i+1
	else:
		print ("dono ki lenght !=")
list_change([5, 10, 50, 20], [2, 20, 3, 5])