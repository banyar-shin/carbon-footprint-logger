from account import UserAccount
import csv
import func
import os
import datetime

def signed_in():
	file = open("csvfiles/usersignedin.csv", "r") # opening the usersignedin file
	data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
	file.close() # closing the file

	if len(data) == 0:
		return False
	elif len(data) == 1:
		return True

def read_in_user():
	file = open("csvfiles/usersignedin.csv", "r") # opening the usersignedin file
	data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
	file.close() # closing the file

	element = data[0]
	return element["userid"], element["username"], element["password"]

def login_or_signup():
	print('''
What would you like to do?
1) Login (Existing User)
2) Sign Up (New User)
3) Main Menu
''')
	
	choices = {"1","2","3"}
	userinput = func.get_input(choices)

	return userinput

def main_screen(currentuser):
	os.system('clear')
	print(f'''
You are signed in as {currentuser.get_username()}.

What would you like to do?
1) Daily Logger
2) Monthly Logger
3) Check History
4) Friends
5) Settings
6) Log Out
7) Close Program
''')
		  
	choices = {"1","2","3","4","5","6"}
	userinput = func.get_input(choices)
	return userinput

def sign_out():
	header = ['userid','username','password']
	with open("csvfiles/usersignedin.csv", 'w') as csvfile: # opening the users signed in file
		writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
		writer.writeheader() # writes the first row in the file as a header
	
	return 0

def menu(currentuser, choice):
	while True:
		if choice == 0:
			choice = main_screen(currentuser)
		elif choice == 1:
			choice = daily_logger(currentuser)
		elif choice == 2:
			choice = currentuser.monthly_logger()
		elif choice == 3:
			choice = currentuser.view_history()
		elif choice == 4:
			choice = currentuser.add_friends()
		elif choice == 5:
			choice = currentuser.set_settings()
		elif choice == 6:
			return sign_out()
		elif choice == 7:
			return 3

def daily_logger(currentuser):
	date = input('''
Welcome to the daily logger!
Please provide the date you want to log.

Enter the date (MM/DD/YYYY): ''')
	while True:
		try:
			logdate = datetime.datetime.strptime(date,"%m/%d/%Y").date()
		except ValueError:
			date = input('''
Invalid date!! >:(
Please provide the date you want to log.

Enter the date again (MM/DD/YYYY): ''')
		else:
			break

	miles = input("")
	
def carbon_footprint(currentuser):
	filename = "csvfiles/" + currentuser.get_userid() + "daily.csv"
	file = open(filename, "r") # opening the user data file
	data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
	file.close() # closing the file

	daily_footprint = (0.0089 * ('ownmiles' / 'carmpg')) + ('diettype' / 365) + ('publicmiles' * 0.08)
	return daily_footprint