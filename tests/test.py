import csv

class UserAccount:
	__userid = "000006"
	__username = "aaronf"
	__password = "Aaron52@"
	__friends = ['000003']
	__outgoing = list()
	__incoming = list()
	__settings = dict()

	# 000002_000003_000005_000004 = string_of_friends

	# dict = {
	# 		'userid': self.__userid,
	#    	'friends': string_of_friends,
	# }
	
	def get_friends(self):
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
		
	def add_friends(self):
		while True:
			file = open("csvfiles/users.csv", "r") # opening the userfriends file
			data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
			file.close() # closing the file

			to_add = input('''
Who would you like to add?
Please enter their username: ''')
			condition = True
			while condition:
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
						to_add = input('''
There is already a pending request.

Enter another username or 'done': ''')
					elif friend_id in self.__friends:
						to_add = input('''
You are already friends with this user.

Enter another username or 'done': ''')
					else:
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

currentuser = UserAccount()
currentuser.add_friends()