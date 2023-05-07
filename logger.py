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
			choice = monthly_logger(currentuser)
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
	os.system('clear')
	date = input('''
Welcome to the daily logger!
Please provide the date you want to log.

Enter the date (MM/DD/YYYY): ''')
	while True:
		try:
			logdate = datetime.datetime.strptime(date,"%m/%d/%Y").date()
		except ValueError:
			os.system('clear')
			date = input('''
Invalid date!
Please provide the date you want to log.

Enter the date again (MM/DD/YYYY): ''')
		else:
			today = datetime.date.today()
			if today >= logdate:
				break
			else:
				os.system('clear')
				date = input('''
This date is in the future.
Please provide the date you want to log.

Enter the date again (MM/DD/YYYY): ''')

	mysettings = currentuser.return_settings()
	
	if mysettings['public'] == '1':
		os.system('clear')
		print(f'''
The date is set to {date}.
Please provide how many miles you traveled using
public transportation on this day.
''')
		publicmiles = func.get_int()
	else: 
		publicmiles = 0
	
	if mysettings['savedvehicle'] != 'none':
		os.system('clear')
		print(f'''
The date is set to {date}.
Please provide how many miles you traveled using
your saved vehicle on this day.
''')
		privatemiles = func.get_int()
	else: 
		privatemiles = 0
		
	RED_MEAT = 3300
	MIXED = 2500
	NO_BEEF = 1900
	VEGETARIAN = 1700
	VEGAN = 1500

	os.system('clear')
	print(f'''
The date is set to {date}.
What did your diet mainly consist of on this day?

1) White Meat Only
2) Meat incl. Red Meat
3) Vegetarian Food
4) Vegan Food
5) Mix of Everything
	''')
	choices = {'1','2','3','4','5'}
	diet = func.get_input(choices)

	dtype = ''
	carbondiet = 0
	
	if diet == 1:
		dtype = 'whitemeat'
		carbondiet = round((NO_BEEF / 365), 2)
	elif diet == 2:
		dtype = 'redmeat'
		carbondiet = round((RED_MEAT / 365), 2)
	elif diet == 3:
		dtype = 'vegetarian'
		carbondiet = round((VEGETARIAN / 365), 2)
	elif diet == 4:
		dtype = 'vegan'
		carbondiet = round((VEGAN / 365), 2)
	elif diet == 5:
		dtype = 'mixed'
		carbondiet = round((MIXED / 365), 2)

	carmpg = int(mysettings['savedvehicle'])
	carbongas = round(((privatemiles / carmpg) * 8.9 + (publicmiles * 0.08)), 2)
	totalcarbon = round((carbongas + carbondiet), 2)
	mydict = {
		'date': date,
		'publicmiles': str(publicmiles),
		'ownmiles': str(privatemiles),
		'carmpg': str(carmpg),
		'diettype': dtype,
		'carbondiet': str(carbondiet),
		'carbongas': str(carbongas),
		'totalcarbon': str(totalcarbon)
			}
	
	filename = "datafiles/" + currentuser.get_userid() + "daily.csv"
	file = open(filename, "r") # opening the users data file
	data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
	file.close() # closing the file

	data.append(mydict)

	header = ['date','publicmiles','ownmiles','carmpg','diettype','carbondiet','carbongas','totalcarbon']
	with open(filename, 'w') as csvfile: # opening the users data file
		writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
		writer.writeheader() # writes the first row in the file as a header
		for element in data:
			writer.writerow(element) # writes each inputted data into a row of the csv file

	print("Your calculated carbon footprint for today is", totalcarbon, "kilograms.")
currentuser = UserAccount()
daily_logger(currentuser)