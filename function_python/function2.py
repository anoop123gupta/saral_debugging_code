def add_number_list(number1,number2):
	for i in number1:
		for j in number2:
			if i==j:
				print (i+j)
add_number_list([2,3,5],[2,4,5])


question_list=["Which country is Delhi located in?","what is the capital of India?","What is the capital of U.P?","what is the captal of Mumbai?","Who is the writer of Ramayan?"]
first_option=["1.India","1.Chandigarh","1.Kanpur","1.Nagpur","1.Vedvyash"]
second_option=["2.USA","2.Bhopal","2.Lucknow","2.Baroda","2.Premchand"]
third_option=["3.France","3.Delhi","3.Jaunpur","3.Thane","3.Mahrshi Valmiki"]
fourth_option=["4.Czech Reblic","4.Jaipur","4.Allahabad","4.Maharastra","4.Harishchandra"]
all_options=[first_option,second_option,third_option,fourth_option]
ans_key=[1,3,2,4,3]
a=0
while a<len(question_list):
	print (question_list[a])
	print (first_option[a])
	print (second_option[a])
	print (third_option[a])
	print (fourth_option[a])
	ans=input("inter your option number-")
	if ans!=ans_key[a]:
		break
	a=a+1
	print ("aap jeet gaye")
else:
	print ("you are paytam winner!")
