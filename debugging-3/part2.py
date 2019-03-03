list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list2 = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
# part 1
def encrypt_message(plain_msg):
	string=" "
	for j in plain_msg:
		i=0
		while i<len(list1):
			if j==list1[i]:
				string+=list2[i]
				break
			i=i+1
	print (string) 
# part 2 
def decrypt_message(encrypted_msg):
	string=" "
	for j in encrypted_msg:
		i=0
		while i<len(list2):
			if j==list2[i]:
				string+=list1[i]
				break
			i=i+1
	print (string)
# part 3

flag = True
while flag:
	choice =input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
	if choice == 'e':
	    plain_message =input("Enter message to encrypt??")
	    encrypt_message(plain_message)
	elif choice == 'd':
	    encrypted_msg =input("Enter message to decrypt?")
	    decrypt_message(encrypted_msg)
	else:
	    play_again =input("Do you want to try again or Do you want to exit? (Y/N)")
	    if play_again == 'Y':
	        continue
	    elif play_again == 'N':
	        break