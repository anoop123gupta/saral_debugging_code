def xmas(num):
    j=8
    for i in range(num):
        print(("*" * (i * 2 + 1)).center(num * 2 - 1))
    print (" "*j+"||"+" "*j)
    print (" "*j+"||"+" "*j)
    print (" "*j+"||"+" "*j)
xmas(10)
name=input("Enter your name : ")
a=input("Enter your wish that you want from Centa: ")
def wish(name,a):
	print ("Marry Chrismas !",name,"May Centa fulfill your wish !")
wish(name,a)

