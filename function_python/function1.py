def ask_question():
	print ("who is founder of facebook ?" )
	print ("mark jukerberg")
	print ("Bill Gates")
	print ("Steve Jobs")
	print ("Larry Page")
i=0
while i<100:
	ask_question()
	i=i+1

###----Examples for understanding------####

def hello(name,language):
	if language=="Hindi":
		print ("Ram Ram ", name )
		print ("kaise ho aap ?")
	elif language=="Punjabi":
		print ("tusssi kithe the ", name)
		print ("rab di mahar hai ")
	else:
		print ("how are you ", name)
		print ("you are learning function ")
hello("Rahul", "Punjabi")
hello("Anoop ", "Tamil")
hello("Ramu","Hindi")
# third example 
def add(num1 , num2 , num3 , num4 , num5):
	print ("This will add all numbers :")
	print (num1+num2+num3+num4+num5)
add(2,2,2,2,2)
add(3,3,3,3,3)


