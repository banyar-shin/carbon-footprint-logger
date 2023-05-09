import csv
import string
import os
import time
import func

class UserAccount:
	__userid = "\0"
	__username = "\0"
	__password = "\0"
	__friends = list()
	__outgoing = list()
	__incoming = list()
	__settings = dict()

	def __init__(self):
		__userid = "\0"
		__username = "\0"
		__password = "\0"
		__friends = list()
		__outgoing = list()
		__incoming = list()
		__settings = dict()
	
	def set_user(self, userid, username, password):
		self.__userid = userid
		self.__username = username
		self.__password = password
	
	def get_userid(self):
		return self.__userid

	def get_username(self): # define function to 
		return self.__username
	
	def return_settings(self): # define function to return user settings
		return self.__settings

	def return_friends(self): #a function to return the friends of the user
		return self.__friends
	
	def assignID(self): # define function to assign id to a new user
		file = open("csvfiles/users.csv", "r") # opening the users file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file
		
		size = len(data) # the size depends on the number of data entries in the file

		userid = str(size + 1) # making the userid a string
		zeros_to_add = 6 - len(userid) # subtracting the number of digits, 7, from the length of the userid

		zeros = "0" * zeros_to_add # the value from the above formula is the number of 0's that we want in front of the id

		self.__userid = zeros + userid # returning the zeros and userid

	def signup_username(self): # define function to set a username and validates
		file = open("csvfiles/users.csv", "r") # opening the users file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file

		allowed = set(string.ascii_lowercase) # create the set for lower letters
		allowed2 = {'1','2','3','4','5','6','7','8','9','_'}
		allowed.update(allowed2)
		os.system('clear')
		username = input('''
Please create your username.

Username requirements:
- Cannot contain symbols other than "_"
- Cannot contain uppercase letters

Enter a username: ''') # ask the user for input
						
		condition = "invalid" # set the condition for a while loop
		while condition == "invalid": # while the condition is invalid, start the while loop
			if len(username) >= 6 and len(username) <= 16: # if the username is 6 or more and 16 or less
				allowed_counter = 0 # initialize the counter for the allowed characters
				for element in username: # read through each element of the username
					if element in allowed: # if the element meets the requirement
						allowed_counter += 1 # increment the counter of the allowed characters
				if allowed_counter == len(username): # if the number of characters in the input is within the margin
					condition = "valid" # set the condition to valid
					
			if condition == "invalid": # if the condition is invalid
				os.system('clear') # clear terminal for cleanliness
				username = input('''
Username is not valid.

Username requirements:
- Cannot contain symbols
- Cannot contain uppercase letters

Enter a username again: ''') # ask the user for input again
			
			elif condition == "valid": # else if the condition is valid
				for element in data: # reading every element of the file
					if username == element["username"]: # if username exists under the usernames of the dictionary
						condition == "invalid" # condition is set to invalid
						os.system('clear') # clear terminal
						username = input('''
Username already exists.

Username requirements:
- Cannot contain symbols
- Cannot contain uppercase letters

Enter the username again: ''') # ask the user for input again
						break
				if condition == "valid": # if the condition is valid
					print("\nYou have successfully chosen your username!")

					time.sleep(0.75) # sleeps for 0.75 seconds
					os.system('clear') # clear terminal

					self.__username = username # return the username
	
	def signup_password(self): # define function to set a password and validate
		letters = set(string.ascii_letters) # create the set for all alphabets
		upper = set(string.ascii_uppercase) # create the set for uppercase letters
		lower = set(string.ascii_lowercase) # create the set for lower letters
		numbers = {'0','1','2','3','4','5','6','7','8','9'} # create the set for numbers
		symbols = {'!','@','#','$','?','*','%','&','~','_'} # create the set for symbols
		os.system('clear')
		password = input('''
Please create your password.

Password Requirements:
- Must have at least 6 characters and at most 12 characters.
- Must include at least one uppercase and one lowercase letter.
- Must include at least 3 numbers or 1 number and 1 symbol.

Enter the password: ''') # Ask the user for input

		condition = "invalid" # set the condition for a while loop
		while condition == "invalid": # while the condition is invalid, start the loop
			if len(password) >= 6 and len(password) <= 12: # if the password length is greater 6 and less than 12
				upper_counter = 0 # initialize the uppercase counter
				lower_counter = 0 # initialize the lowercase counter
				number_counter = 0 # initialize the number counter
				for element in password: # read through each element in the password
					if element in upper: # if the element is the uppercase
						upper_counter += 1 # increment the uppercase counter
					if element in lower: # if the element is the lowercase
						lower_counter += 1 # increment the lowercase counter
					if element in numbers: # if the element is the number
						number_counter += 1 # increment the number counter
				if upper_counter >= 1 and lower_counter >= 1 and number_counter >= 1: #if there is an uppercase, lowercase and the number in the password
					base = pow(52,len(password)-2) * 62 * 72 # set the base 
					com = 1 # initialize the combination of the password
					for element in password: # read through every element in password
						if element in letters: # if the element is a letter
							com = com * 52 # com times 52
						if element in numbers: # if the element is a number
							com = com * 62 # com times 62
						if element in symbols: # if the element is a symbol
							com = com * 72 # com times 72
					if com >= base: # if com is greater than or equal to base
						condition = "valid" # set the condition to valid
			if condition == "invalid": # if the condition is invalid
				os.system('clear') # clears the terminal
				password = input('''
Password is not strong enough, please try again.

Password Requirements:
- Must have at least 6 characters and at most 12 characters.
- Must include at least one uppercase and one lowercase letter.
- Must include at least 3 numbers or 1 number and 1 symbol.

Enter the password: ''') # ask the user for input again
			elif condition == "valid": # else if the condition is valid
				os.system('clear')
				re_enter = input('''
Please confirm your password by re-entering it.

Enter the password: ''') # ask the user for input again
				if re_enter == password:
					print("\nYou have successfully created a password!") # create the password
					time.sleep(0.75) # sleeps for 0.75 seconds
					os.system('clear') # clears the terminal
					self.__password = password # return the password
				else:
					condition = "invalid"

	def set_settings(self): # define function to set the user's settings
		file = open("csvfiles/usersettings.csv", "r") # opening the settings file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file

		mydict = {
			'userid': self.__userid,
			'public': '0',
			'savedvehicle': 'none',
			'household': '0',
			'recycle': '0',
					}
		os.system('clear')
		print('''
Now, we will be setting your preferences.

Do you use public transportation regularly?
1) Yes
2) No
''')
		choices = {"1","2"}
		choice = func.get_input(choices)
		if choice == 1:
			mydict['public'] = '1'

		os.system('clear')
		print('''
Do you use have your own car or motorcycle?
1) Yes
2) No
''')
		choices = {"1","2"}
		choice = func.get_input(choices)
		if choice == 1:
			os.system('clear')
			print('''
How many miles per gallon do you get?
Range of answers: 5 - 120.

Typical MPGs:
- Motorcycle: 45
- Car/Sedan/SUV: 23
- Light Truck/Van: 17
- Delivery Truck: 12
''')
			mpgs = set()
			for i in range(5,121):
				mpgs.add(str(i))
			savedvehicle = func.get_input(mpgs)
			mydict['savedvehicle'] = savedvehicle
		
		os.system('clear')
		print('''
What is the size of your household?
Range of answers: 1 - 6 (Use 6 for 6 or more).
''')
		choices = {"1","2","3","4","5","6"}
		household = func.get_input(choices)

		mydict['household'] = household
	
		os.system('clear')
		print('''
Do you recycle items such as metal, plastic, glass, or paper?

1) Yes
2) No
''')
		choices = {"1","2"}
		choice = func.get_input(choices)
		if choice == 1:
			mydict['recycle'] = '1'
		
		self.__settings = mydict

		for element in data:
			if element['userid'] == self.__userid:
				data.remove(element)

		data.append(mydict)

		header = ['userid','public','savedvehicle','household','recycle']
		with open("csvfiles/usersettings.csv", 'w') as csvfile: # opening the users signed in file
			writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
			writer.writeheader() # writes the first row in the file as a header
			for element in data:
				writer.writerow(element) # writes each inputted data into a row of the csv file

		print("\nYou have successfully finished setting up!") # create the password
		time.sleep(0.75) # sleeps for 0.75 seconds
		os.system('clear') # clears the terminal

		return 0

	def get_settings(self): # define function to get existing user's settings
		file = open("csvfiles/usersettings.csv", "r") # opening the settings file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file

		for element in data:
			if element['userid'] == self.__userid:
				self.__settings = {
					'userid': self.__userid,
					'public': element['public'],
					'savedvehicle': element['savedvehicle'],
					'household': element['household'],
					'recycle': element['recycle'],
				}
				break

	def login_username(self): # define function to use existing username
		file = open("csvfiles/users.csv", "r") # opening the users file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file

		os.system('clear')
		username = input('''
First, you'll need your username to log in.

Enter your username: ''') # ask the user for input
		found = False
		while found == False:
			for element in data:
				if username == element['username']:
					self.__username = username
					self.__userid = element['userid']
					self.__password = element['password']
					found = True
					break
			else:
				os.system('clear')
				username = input('''
No existing account with such username found.

Enter your username again: ''') # ask the user for input
		
	def login_password(self): # define function to use existing password
		os.system('clear')
		password = input('''
Next, you'll need the password to your account.

Enter your password: ''')
		counter = 5
		while True:
			if counter == 1:
				return 0
			if password != self.__password:
				counter -= 1
				os.system('clear')
				password = input(f'''
Your password is wrong. You have {counter} more tries.

Enter your password again: ''')
			elif password == self.__password:
				break

	def get_friends(self): # define function to get friends into object
		file = open("csvfiles/userfriends.csv", "r") # opening the userfriends file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file
		for element in data: # read through each element of the data
			if element['userid'] == self.__userid: # if the userid is in the list
				if element['friends'].split("_") != ['']: # check if it empty
					self.__friends = element['friends'].split("_") # set friends
				if element['outgoing'].split("_") != ['']: # check if it empty
					self.__outgoing = element['outgoing'].split("_") # set outgoing requests
				if element['incoming'].split("_") != ['']: # check if it empty
					self.__incoming = element['incoming'].split("_") # set incoming requests
				break
		
	def add_friends(self): # define function to allow user to add friends
		to_add = ''
		while True:
			if to_add == 'done':
				break
			file = open("csvfiles/users.csv", "r") # opening the userfriends file
			data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
			file.close() # closing the file
			os.system('clear')
			to_add = input('''
Who would you like to add?

Please enter their username or 'done': ''')
			if to_add == 'done':
				break
			condition = True
			while condition:
				friend_id = " "
				if to_add == 'done':
					break
				for element in data:
					if element['username'] == to_add and to_add != self.__username: #if the username existed
						friend_id = element['userid']
						if friend_id not in self.__outgoing and friend_id not in self.__friends:
							self.__outgoing.append(friend_id)
							condition = False
							break
				if to_add == 'done':
					break
				elif condition:
					if friend_id in self.__outgoing:
						os.system('clear')
						to_add = input('''
There is already a pending request.

Enter another username or 'done': ''')
					elif friend_id in self.__friends:
						os.system('clear')
						to_add = input('''
You are already friends with this user.

Enter another username or 'done': ''')
					else:
						os.system('clear')
						to_add = input('''
Username does not exist.
Enter another username or 'done': ''')
			if to_add == 'done':
				break
		
			file = open("csvfiles/userfriends.csv", "r") # opening the userfriends file
			data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
			file.close() # closing the file

			for element in data:
				if element['userid'] == friend_id:
					incoming_entry = element
					if element['incoming'].split("_") != ['']:
						incoming_list = element['incoming'].split("_")
					else:
						incoming_list = list()
					data.remove(element)
					break
			
			incoming_list.append(self.__userid)
			incoming_str = '_'.join(incoming_list)
			incoming_entry['incoming'] = incoming_str

			data.append(incoming_entry)

			header = ['userid', 'friends', 'outgoing', 'incoming']
			with open("csvfiles/userfriends.csv", 'w') as csvfile: # opening the users signed in file
				writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
				writer.writeheader() # writes the first row in the file as a header
				for element in data:
					writer.writerow(element) # writes each inputted data into a row of the csv file

		file = open("csvfiles/userfriends.csv", "r") # opening the userfriends file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file

		for element in data:
			if element['userid'] == self.__userid:
				outgoing_entry = element
				data.remove(element)
				break

		outgoing_str = '_'.join(self.__outgoing)
		outgoing_entry['outgoing'] = outgoing_str

		data.append(outgoing_entry)

		header = ['userid', 'friends', 'outgoing', 'incoming']
		with open("csvfiles/userfriends.csv", 'w') as csvfile: # opening the users signed in file
			writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
			writer.writeheader() # writes the first row in the file as a header
			for element in data:
				writer.writerow(element) # writes each inputted data into a row of the csv file
		return 0

	def pending_requests(self): # define funtion to allow user to accept pending requests
		file = open("csvfiles/users.csv", "r") # opening the userfriends file
		users = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file
		
		mylist = self.__incoming

		if len(mylist) != 0:
			for element in users:
				for person in mylist:
					if person == element['userid']:
						os.system('clear')
						print(f'''					
{element['username']} wants to add you!

1) Accept Friend Request
2) Deny Friend Request
''')
						choices = {"1","2"}
						choice = func.get_input(choices)

						if choice == 1:
							file = open("csvfiles/userfriends.csv", "r") # opening the userfriends file
							data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
							file.close() # closing the file
							
							for element2 in data:
								if person == element2['userid']:
									outgoing_entry = element2
									if element2['outgoing'].split("_") != ['']:
										outgoing_list = element2['outgoing'].split("_")
									if element2['friends'].split("_") != ['']:
										friends_list = element2['friends'].split("_")
									else:
										friends_list = list()
										outgoing_list = list()
									data.remove(element2)
									break
							
							for element2 in outgoing_list:
								if element2 == self.__userid:
									outgoing_list.remove(element2)
									break
							outgoing_str = '_'.join(outgoing_list)
							outgoing_entry['outgoing'] = outgoing_str

							friends_list.append(self.__userid)
							friends_str = '_'.join(friends_list)
	
							outgoing_entry['friends'] = friends_str

							data.append(outgoing_entry)

							for element in data:
								if element['userid'] == self.__userid:
									data.remove(element)
									break
									
							self.__friends.append(person)
							self.__incoming.remove(person)

							friends_str2 = '_'.join(self.__friends)
							incoming_str2 = '_'.join(self.__incoming)
							outgoing_str2 = '_'.join(self.__outgoing)

							incoming_entry = {
								'userid': self.__userid,
								'friends': friends_str2,
								'outgoing': outgoing_str2,
								'incoming': incoming_str2 
							}
							
							data.append(incoming_entry)

							header = ['userid', 'friends', 'outgoing', 'incoming']
							with open("csvfiles/userfriends.csv", 'w') as csvfile: # opening the users signed in file
								writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
								writer.writeheader() # writes the first row in the file as a header
								for element in data:
									writer.writerow(element) # writes each inputted data into a row of the csv file
									
						if choice == 2:
							file = open("csvfiles/userfriends.csv", "r") # opening the userfriends file
							data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
							file.close() # closing the file
							
							for element2 in data:
								if person == element2['userid']:
									outgoing_entry = element2
									if element2['outgoing'].split("_") != ['']:
										outgoing_list = element2['outgoing'].split("_")
									else:
										outgoing_list = list()
									data.remove(element2)
									break
							
							for element2 in outgoing_list:
								if element2 == self.__userid:
									outgoing_list.remove(element2)
									break
							outgoing_str = '_'.join(outgoing_list)
							outgoing_entry['outgoing'] = outgoing_str

							data.append(outgoing_entry)

							for element in data:
								if element['userid'] == self.__userid:
									data.remove(element)
									break
									
							self.__incoming.remove(person)

							friends_str = '_'.join(self.__friends)
							incoming_str = '_'.join(self.__incoming)
							outgoing_str = '_'.join(self.__outgoing)

							incoming_entry = {
								'userid': self.__userid,
								'friends': friends_str,
								'outgoing': outgoing_str,
								'incoming': incoming_str 
							}
							
							data.append(incoming_entry)

							header = ['userid', 'friends', 'outgoing', 'incoming']
							with open("csvfiles/userfriends.csv", 'w') as csvfile: # opening the users signed in file
								writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
								writer.writeheader() # writes the first row in the file as a header
								for element in data:
									writer.writerow(element) # writes each inputted data into a row of the csv file
			os.system('clear')
			print('''
Those were all of the requests.

Taking you back...
	''')
			time.sleep(2)
			return 0
		else:
			os.system('clear')
			print('''
You have no incoming requests.

Taking you back...
	''')
		time.sleep(2)
		return 0

	def save_user(self): # define function to save user details to file
		file = open("csvfiles/users.csv", "a") # opening the users file
		to_write = "\n" + self.__userid + "," + self.__username + "," + self.__password # making a string for the user information
		file.write(to_write) # appending the userid, username, and password to file
		file.close() # closing the file

		filename = "datafiles/" + self.__userid + "daily.csv" # creating a file
		file = open(filename, "x") # opening the users data 
		file.close() # closing the file

		filename = "datafiles/" + self.__userid + "monthly.csv" # creating a file
		file = open(filename, "x") # opening the users data file
		file.close() # closing the file

		mydict = {
			'userid': self.__userid,
			'friends': '',
			'outgoing': '',
			'incoming': ''
			}
		
		file = open("csvfiles/userfriends.csv", "r") # opening the userfriends file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file

		data.append(mydict)

		header = ['userid', 'friends', 'outgoing', 'incoming']
		with open("csvfiles/userfriends.csv", 'w') as csvfile: # opening the users signed in file
			writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
			writer.writeheader() # writes the first row in the file as a header
			for element in data:
				writer.writerow(element) # writes each inputted data into a row of the csv file

	def stay_signed_in(self): # define function to allow user to be signed in
		os.system('clear')
		stay = input('''
Would you like to stay signed-in?

Enter Y/N (or) y/n: ''') # asking user if they want to stay signed-in
		if stay.lower() == "y": # if the user says yes
			csv_headers = ['userid','username','password'] # setting the headers of the file
			userdata = {'userid': self.__userid, 'username': self.__username, 'password': self.__password} # setting the data that will be stored into the file
			with open("csvfiles/usersignedin.csv", 'w') as csvfile: # opening the users signed in file
				writer = csv.DictWriter(csvfile, fieldnames = csv_headers) # writing a csv file to the dictionary
				writer.writeheader() # writes the first row in the file as a header
				writer.writerow(userdata) # writes each inputted data into a row of the csv file