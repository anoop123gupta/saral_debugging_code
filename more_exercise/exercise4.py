num=int(input("Enter a number :"))
i=1
fact=1
while i<=num:
	fact=fact*i
	i+=1
print ("Factorial of ", num ,"is ", fact)
# second method using range 
# fact =1
# for i in range(1,num+1):
# 	fact=fact*i
# 	i+=1
# print (fact)