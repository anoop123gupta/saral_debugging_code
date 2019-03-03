# part 1
def check_numbers(a,b):
		print (a+b)
check_numbers(2,6)

# part 2 

def check_numbers_list(a,b):
	i=0
	if len(a)==len(b):
		while i<len(a):
			check_numbers(a[i],b[i])
			i +=1
	else:
		print ("lists ki len barabar nahi hai")
check_numbers_list([10,30,40],[40,20,21])

