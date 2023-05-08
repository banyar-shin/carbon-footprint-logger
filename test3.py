import func
import os
import time
import csv
# from account import UserAccount

class UserAccount:
	__userid = "000000"
	__username = "thirii"
	__password = "Thiri123"
	__friends = ['000001']
	__outgoing = ['000003']
	__incoming = ['000004']
	__settings = dict()

	def get_username(self): # define function to 
		return self.__username
	
	def get_userid(self):
		return self.__userid

	def return_friends(self): #a function to return the friends of the user
		return self.__friends

def friends_menu(currentuser):#this fucn let the user to add friends and check their daily logger
	os.system('clear')
	print('''
Here is where you can interact with your friends!

What would you like to do?
1) Friends' Activities
2) Add Friends
3) Check Pending Requests
4) Back to Main Menu
''')#print the menu
	choices = {"1","2","3"} #create a dictionary for choices
	choice = func.get_input(choices) #get the choices from user
	if choice == 1: #if choice is one
		while True:
			os.system('clear')
			userfriendsname = input('''
Which friend would you like to see?

Enter their username: ''')

			filename = "csvfiles/users.csv"
			file = open(filename, "r") # open it in read mode
			data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
			file.close() # closing the file
			found = False
			for element in data:
				if element['username'] == userfriendsname:
					found = True
					friendsID = element['userid']
					break
			if not found:
				print("Username was not found.")
				time.sleep(1)
				continue

			if friendsID in currentuser.return_friends():
				filename = "csvfiles/todaysdata.csv" #open the userfriends csv file
				file = open(filename, "r") # open it in read mode
				data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
				file.close() # closing the file
				print("\nHere's today's data for your friend, " + userfriendsname + ":\n" )
				for item in data:
					if item['userid'] == friendsID:
						if item['publicmiles'] != '0':
							print("- Miles traveled using public transportation today: " + item['publicmiles'] + " miles.")
						if item['ownmiles'] != '0':
							print("- Miles driven on their own vehicle today: " + item['ownmiles'] + " miles.")
						print(f'''- What their diet consisted of today: {item['diettype']} kilograms.
- Carbon dioxide emitted from food today: {item['carbondiet']} kilograms.
- Carbon dioxide emitted transportation today: {item['carbongas']} kilograms.
- Total carbon dioxide emitted today: {item['totalcarbon']} kilograms.

What would you like to do now?

1) Another User
2) Go Back
''')
						choices = {"1","2"}
						choice = func.get_input(choices)
						if choice == "2":
							return 0
			else:
				print('''
You are not friends with this user.
What would you like to do?

1) Another User
2) Go Back
''')
				choices = {"1","2"}
				choice = func.get_input(choices)
				if choice == "2":
					return 0
	if choice == 2:#if 
		currentuser.add_friends()
	if choice == 3:
		func.quit_program()
		time.sleep(3)


currentuser = UserAccount()
friends_menu(currentuser)