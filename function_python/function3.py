def add_number(a,b):
	print (a+b)
add_number(4,6)
# part 2
def add_number_list(a,b):
	i=0
	if len(a)==len(b):
		while i<len(a):
			add_number(a[i],b[i])
			i=i+1
	else:
		print (" len == nhi hai ")
add_number_list([10,20,22],[20,25,18])
