# # def encrypt():
# #   message = input("Enter the message you want to encrypt")
# #   ascii_message = [ord(char)+3 for char in message]
# #   encrypt_message = [ chr(char) for char in ascii_message]  
# #   print(''.join(encrypt_message))
# # encrypt()

# # def decrypt():
# #     message = input("Enter the message you want to decrypt")
# #     ascii_message = [ord(char) for char in message]
# #     decrypt_message = [ chr(char) for char in ascii_message]  
# #     print (decrypt_message)
# # decrypt()
# # # flag = True
# # # while flag == True:
# # #     choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
# # #     if choice == 'e':
# # #         encrypt()
# # #     elif choice == 'd':
# # #         decrypt()    
# # #     play_again =input("Do you want to try agian or Do you want to exit? (Y/N)")
# # #     if play_again == 'Y':
# # #         continue
# # #     elif play_again == 'N':
# # #         break
# def find_in_list(query, mainlist):
# # this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
#     mainlist_len = len(mainlist)
#     range_for_loop = range(mainlist_len)
#     index = None
#     for i in range_for_loop:
#         element = mainlist[i]
#         if element == query:
#             index = i
#             break
#     return index
# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
# def encrypt_message(plain_msg):
# # this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
#     encrypted_msg = ""
#     for character in plain_msg:
#       # for character in msg
#         if character in chars:
#             char_index = find_in_list(character, chars)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char
#         else:
#             encrypted_msg = encrypted_msg + character
#     return encrypted_msg
# print (encrypt_message("vishal"))
# #decrypt_message function defined here but not called
# def decrypt_message(encrypted_msg):
# # this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
#     decrypted_msg = ""
#     for character in encrypted_msg:
#         if character in shifted_chars:
#             char_index = find_in_list(character, shifted_chars)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + character
#     return decrypted_msg
# print (decrypt_message("xkujcn"))

# # methods should return or print the new messages.
# # ############################################### Code starts from here ##################################################
# flag = True
# while flag==True:
# 	choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
# 	if choice == 'e':
# 	    plain_message = input("Enter message to encrypt?? ")
# 	    print (encrypt_message(plain_message))
# 	elif choice == 'd':
# 	    encrypted_msg = input("Enter message to decrypt?")
# 	    decrypt_message(encrypted_msg)
# 	else:
# 	    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
# 	    if play_again == 'Y':
# 	        continue
# 	    elif play_again == 'N':
#     		break

# from random import randint # allows you to generate a random number

# # variables for the alien
# alive = True
# stamina = 10

# # this function runs each time you attack the alien
# def report(s):
# # syntactic error in if else statements
#     if s > 8:
#         print ("The alien is strong! It resists your pathetic attack!")
#     elif s > 5:
#         print ("With a loud grunt, the alien stands firm.")
#     elif s > 3:
#         print ("Your attack seems to be having an effect! The alien stumbles!")
#     elif s > 0:
#         print ("The alien is certain to fall soon! It staggers and reels!")
#     else:
#         print ("That's it! The alien is finished!")

# # main function - accepts your input for fight with the alien
# def fight(stam): # stamina
#     while stam < 0:
#       # won't enter this loop ever. The function will always return False.
#         response =input("> Enter a move 1.Hit 2.attack 3.fight 4.run ")
#         # chose a response from ( hit, attack, fight and run)
#         # fight scene
#         if "hit" in response or "attack" in response:
#             less = randint(0, stam)
#             stam -= less # subtract random int from stamina
#             report(stam) # see function above
#         if "fight" in response:
#             print ("Fight how? You have no weapons, silly space traveler!")
#         elif "run" in response:
#             print ("Sadly, there is nowhere to run.",)
#             print ("The spaceship is not very big.")
#         else:
#             print ("The alien zaps you with its powerful ray gun!")
#         return True
#     return False
# print ("A threatening alien wants to fight you!")
# # quotes at the end.

# # call the function - what it returns will be the value of alive
# alive = fight(stamina)

# if alive: # means if alive == True
#     print ("\nThe alien lives on, and you, sadly, do not.\n")
# else:
#     print ("\nThe alien has been vanquished. Good work!\n")
#     
def encrypt():
  message = input("Enter the message you want to encrypt ")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))
encrypt()

def decrypt():
  message = input("Enter the message you want to decrypt ")
  ascii_message = [ord(char)-3 for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))
decrypt()

flag = True
while flag == True:
	choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively! ")
	if choice == 'e':
		encrypt()
	elif choice == 'd':
		decrypt()
		break    
	else:
	    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
	    if play_again == 'Y':
	    	continue
	    elif play_again == 'N':
        	break