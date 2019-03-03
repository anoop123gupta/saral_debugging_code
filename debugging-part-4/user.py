import json
with open('users.json') as data_file:    
    data = json.load(data_file)

users = data['users']

for user in users:
	counter = 0
	print ("users full name is " + user['firstName'] + ' ' + user['lastName'])
	while counter < len(user['details']):
		print ("users mobile number is " , user['details']['mobileNo'])
		print ("users age  is " , user['details']['age'])
		print ("users city is " , user['details']['City'])
		counter+=3 