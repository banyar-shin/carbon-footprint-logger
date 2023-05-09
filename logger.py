from account import UserAccount
import csv
import func
import os
import datetime
import time

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

def check_date():
	today = datetime.date.today()
	d1 = today.strftime("%m/%d/%Y")
	file = open("csvfiles/todaysdata.csv", "r") # opening the users data file
	data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
	file.close() # closing the file
	for element in data:
		if element['date'] != d1:
			data.remove(element)
			
	header = ['userid','date','publicmiles','ownmiles','carmpg','diettype','carbondiet','carbongas','totalcarbon'] # setting the header of the file
	with open("csvfiles/todaysdata.csv", 'w') as csvfile: # opening the users data file
		writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
		writer.writeheader() # writes the first row in the file as a header
		for element in data:
			writer.writerow(element) # writes each inputted data into a row of the csv file
		csvfile.close()

def main_screen(currentuser):
	os.system('clear')
	check_date()
	print(f'''
You are signed in as {currentuser.get_username()}.

What would you like to do?
1) Daily Logger
2) Monthly Logger
3) View Logs
4) Friends
5) Settings
6) Log Out
7) Close Program
''')
		  
	choices = {"1","2","3","4","5","6","7"}
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
			choice = view_history(currentuser)
		elif choice == 4:
			choice = friends_menu(currentuser)
		elif choice == 5:
			choice = currentuser.set_settings()
		elif choice == 6:
			return sign_out()
		elif choice == 7:
			return 3

def daily_logger(currentuser): # defining function for the daily logger
	os.system('clear')

	filename = "datafiles/" + currentuser.get_userid() + "daily.csv" # creating a file
	file = open(filename, "r") # opening the users data file
	data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
	file.close() # closing the file

	td = False

	date = input('''
Welcome to the daily logger!
Please provide the date you want to log.

Enter the date (MM/DD/YYYY): ''') # ask user to input the date they want to log their data
	while True: # while they input a date that is valid
		try:
			logdate = datetime.datetime.strptime(date,"%m/%d/%Y").date() # using the datetime library to check the formatting of the date
		except ValueError: # incorrect formatting of the date
			os.system('clear')
			date = input('''
Invalid date!
Please provide the date you want to log.

Enter the date again (MM/DD/YYYY): ''') # telling user to correct the format of their date
		else:
			today = datetime.date.today() # today's date
			if today >= logdate: # if the inputted date is less than or equal to today's date
				exists = False
				for element in data:
					if date == element['date']:
						exists = True
				if exists == False:
					if today == logdate:
						td = True
					break
				else:
					os.system('clear')
					date = input('''
There is already a log for this date.
You may view this log in "View Logs".
Please provide another date.

Enter the date again (MM/DD/YYYY): ''') # tell the user to input a valid date, since it's in the future
			else: # but if the inputted date is greater than today's date
				os.system('clear')
				date = input('''
This date is in the future.
Please provide the date you want to log.

Enter the date again (MM/DD/YYYY): ''') # tell the user to input a valid date, since it's in the future

	mysettings = currentuser.return_settings()
	
	if mysettings['public'] == '1': # if the user regularly takes public transportation
		os.system('clear')
		print(f'''
The date is set to {date}.
Please provide how many miles you traveled using
public transportation on this day.
''') # ask the user how many miles they publically traveled in
		publicmiles = int(func.get_int()) # accepting the number of miles in integers
	else: 
		publicmiles = 0 # otherwise, they didn't use public transportation that day
	
	if mysettings['savedvehicle'] != 'none': # if the user has a vehicle saved
		os.system('clear')
		print(f'''
The date is set to {date}.
Please provide how many miles you traveled using
your saved vehicle on this day.
''') # ask the user how many miles they traveled with their saved vehicle
		privatemiles = int(func.get_int()) # accepting the number of miles in integers
		carmpg = int(mysettings['savedvehicle']) # accessing the data for savedvehicle in users settings to get their vehicle's mpg
	else: 
		privatemiles = 0 # otherwise, they didn't use their saved vehicle that day
		carmpg = 1

	RED_MEAT = 3300 # the dietary footprint of consuming meat(including red meat) in kilograms of CO2 per year
	MIXED = 2500 # the dietary footprint of consuming a variety of foods in kilograms of CO2 per year
	NO_BEEF = 1900 # the dietary footprint of consuming meat(w/o red meat) in kilograms of CO2 per year
	VEGETARIAN = 1700 # the dietary footprint of consuming vegetarian food in kilograms of CO2 per year
	VEGAN = 1500 # the dietary footprint of consuming vegan food in kilograms of CO2 per year

	os.system('clear')
	print(f'''
The date is set to {date}.
What did your diet mainly consist of on this day?

1) White Meat Only
2) Meat incl. Red Meat
3) Vegetarian Food
4) Vegan Food
5) Mix of Everything
	''') # asking the user of their main diet for that day my providing the diets to choose from
	choices = {'1','2','3','4','5'} # creating the choices for the user to pick from
	diet = func.get_input(choices) # allowing the user to only pick from the 1-5 choices

	dtype = ''
	carbondiet = 0 # initiating the carbon diet
	
	if diet == 1: # if the user picks 1
		dtype = 'whitemeat' # set their diet type to whitemeat
		carbondiet = round((NO_BEEF / 365), 2) # dividing the dietary footprint by number of days in a year to get the carbon diet
	elif diet == 2: # if the user picks 2
		dtype = 'redmeat' # set their diet type to redmeat
		carbondiet = round((RED_MEAT / 365), 2) # dividing the dietary footprint by number of days in a year to get the carbon diet
	elif diet == 3: # if the user picks 3
		dtype = 'vegetarian' # set their diet type to vegetarian
		carbondiet = round((VEGETARIAN / 365), 2) # dividing the dietary footprint by number of days in a year to get the carbon diet
	elif diet == 4: # if the user picks 4
		dtype = 'vegan' # set their diet type to vegan
		carbondiet = round((VEGAN / 365), 2) # dividing the dietary footprint by number of days in a year to get the carbon diet
	elif diet == 5: # if the user picks 5
		dtype = 'mixed' # set their diet type to mixed
		carbondiet = round((MIXED / 365), 2) # dividing the dietary footprint by number of days in a year to get the carbon diet

	carbongas = round(((privatemiles / carmpg) * 8.9 + (publicmiles * 0.08)), 2) # formula to find their carbon gas
	totalcarbon = round((carbongas + carbondiet), 2) # getting their total carbon footprint by adding the carbon gas and diet
	mydict = {
		'date': date,
		'publicmiles': str(publicmiles),
		'ownmiles': str(privatemiles),
		'carmpg': str(carmpg),
		'diettype': dtype,
		'carbondiet': str(carbondiet),
		'carbongas': str(carbongas),
		'totalcarbon': str(totalcarbon)
			} # listing the data for the dictionary of the daily loggger

	data.append(mydict) # appending the dictionary

	header = ['date','publicmiles','ownmiles','carmpg','diettype','carbondiet','carbongas','totalcarbon'] # setting the header of the file
	with open(filename, 'w') as csvfile: # opening the users data file
		writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
		writer.writeheader() # writes the first row in the file as a header
		for element in data:
			writer.writerow(element) # writes each inputted data into a row of the csv file
		csvfile.close()

	if td:
		file = open("csvfiles/todaysdata.csv", "r") # opening the users data file
		data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
		file.close() # closing the file

		mydict["userid"] = currentuser.get_userid()
		data.append(mydict)

		header = ['userid','date','publicmiles','ownmiles','carmpg','diettype','carbondiet','carbongas','totalcarbon'] # setting the header of the file
		with open("csvfiles/todaysdata.csv", 'w') as csvfile: # opening the users data file
			writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
			writer.writeheader() # writes the first row in the file as a header
			for element in data:
				writer.writerow(element) # writes each inputted data into a row of the csv file
			csvfile.close()

	print("\nYour calculated carbon footprint for this day is", totalcarbon, "kilograms.") # outputting the total carbon footprint for the user to see

	if totalcarbon < 19.74:
		print("\nYou did better than the average person!")
	else:
		print("\nYou did worse than the average person.")

	time.sleep(3)
	return 0
	
def carbonhome(x):
	mylist = [982.8, 926.1, 869.4, 812.7, 756, 699.3]
	return mylist[x - 1]

def monthly_logger(currentuser):
	os.system('clear')

	filename = "datafiles/" + currentuser.get_userid() + "monthly.csv" # creating a file
	file = open(filename, "r") # opening the users data file
	data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
	file.close() # closing the file

	date = input('''
Welcome to the monthly logger!
Please provide the month you want to log.

Enter the month (MM/YYYY): ''') # ask user to input the date they want to log their data
	while True: # while they input a date that is valid
		try:
			logdate = datetime.datetime.strptime(date,"%m/%Y").date() # using the datetime library to check the formatting of the date
		except ValueError: # incorrect formatting of the date
			os.system('clear')
			date = input('''
Invalid date!
Please provide the month you want to log.

Enter the month again (MM/YYYY): ''') # telling user to correct the format of their date
		else:
			today = datetime.date.today() # today's date
			if today >= logdate: # if the inputted date is less than or equal to today's date
				exists = False
				for element in data:
					if date == element['date']:
						exists = True
				if exists == False:
					break
				else:
					os.system('clear')
					date = input('''
There is already a log for this month.
Please provide another month.

Enter the date again (MM/YYYY): ''') # tell the user to input a valid date, since it's in the future
			else: # but if the inputted date is greater than today's date
				os.system('clear')
				date = input('''
This month is in the future. 
Please provide the month you want to log.

Enter the month again (MM/YYYY): ''') # tell the user to input a valid date, since it's in the future
	
	os.system('clear')

	print(f'''
Please provide the number of short round-trips that you have flown in the past month.
Short flights are less than 300 miles.
''') # ask user for number of short round-trips
	shortflight = int(func.get_int()) # allowing user to type an integer
	shortcarbon = shortflight * 75 # multiply the number of flights with 75 kg, which is the average amount of CO2 emitted per short flight
	
	os.system('clear')
	print(f'''
Please provide the number of medium round-trips that you have flown in the past month.
Medium flights are 300 - 2500 miles.
''') # ask user for number of medium round-trips
	medflight = int(func.get_int())# allowing user to type an integer
	medcarbon = medflight * 395 # multiply the number of flights with 395 kg, which is the average amount of CO2 emitted per medium flight

	os.system('clear')
	print(f'''
Please provide the number of long round-trips that you have flown in the past month.
Long flights are over 2500 miles.
''') # ask user for number of long trips
	longflight = int(func.get_int()) # allowing user to type an integer
	longcarbon = longflight * 845 # multiply the number of flights with 845 kg, which is the average amount of CO2 emitted per long flight

	carbonflight = shortcarbon + medcarbon + longcarbon # adding the CO2 emitted to calculate the total carbon from flights

	mysettings = currentuser.return_settings() # accessing the user settings
	
	home = 0 # initializing carbonhome
	if mysettings['household'] == '1': # if the user's household has 1 person
		home = carbonhome(1) # set their home carbon footprint to 982.8 kg/mo
	elif mysettings['household'] == '2': # if the user's household has 2 people
		home = carbonhome(2) # set their home carbon footprint to 926.1 kg/mo
	elif mysettings['household'] == '3': # if the user's household has 3 people
		home = carbonhome(3) # set their home carbon footprint to 869.4 kg/mo
	elif mysettings['household'] == '4': # if the user's household has 4 people
		home = carbonhome(4) # set their home carbon footprint to 812.7 kg/mo
	elif mysettings['household'] == '5': # if the user's household has 5 people
		home = carbonhome(5) # set their home carbon footprint to 756.0 kg/mo
	elif mysettings['household'] == '6': # if the user's household has 6 or more people
		home = carbonhome(6) # set their home carbon footprint to 699.3 kg/mo

	totalcarbon = carbonflight + home # calculating the total carbon footprint by adding the carbon emitted from flights and home
	

	mydict = {
		'date': date,
		'shortflights': str(shortflight),
		'mediumflights': str(medflight),
		'longflights': str(longflight),
		'carbonflight': str(carbonflight),
		'carbonhome': str(home),
		'totalcarbon': str(totalcarbon)
			} # listing data from dictionary

	data.append(mydict) # appending the dictionary

	header = ['date','shortflights','mediumflights','longflights','carbonflight','carbonhome','totalcarbon'] # setting the header of the file
	with open(filename, 'w') as csvfile: # opening the users data file
		writer = csv.DictWriter(csvfile, fieldnames = header) # writing a csv file to the dictionary
		writer.writeheader() # writes the first row in the file as a header
		for element in data:
			writer.writerow(element) # writes each inputted data into a row of the csv file

	print("\nYour calculated carbon footprint for this month is", totalcarbon, "kilograms.") # outputting the total carbon footprint for the user to see

	if totalcarbon < 1428.3:
		print("\nYou did better than the average person!")
	else:
		print("\nYou did worse than the average person.")
	
	time.sleep(3)
	return 0

def view_history(currentuser):
	while True:
		os.system('clear')
		print('''
You can view and edit your past logs here.
Which category do you want to view?

1) Daily Logs
2) Go Back
''')
		choices = {"1","2"}
		choice = func.get_input(choices)

		if choice == 1:
			filename = "datafiles/" + currentuser.get_userid() + "daily.csv" #open the userfriends csv file
			file = open(filename, "r") # open it in read mode
			data = list(csv.DictReader(file, delimiter=",")) # accessing the data under the file
			file.close() # closing the file
			date = input('''
Please enter the date you'd like to look up.

Enter the date (MM/DD/YYYY): ''') # ask user to input the date they want to log their data
			while True: # while they input a date that is valid
				try:
					logdate = datetime.datetime.strptime(date,"%m/%d/%Y").date() # using the datetime library to check the formatting of the date
				except ValueError: # incorrect formatting of the date
					os.system('clear')
					date = input('''
Invalid date!
Please enter the date you'd like to see.

Enter the date again (MM/DD/YYYY): ''') # telling user to correct the format of their date
				else:
					found = False
					for element in data:
						if date == element['date']:
							found = True
							os.system('clear')
							print (f"Here's your data for {date}:\n")
							if element['publicmiles'] != '0':
								print("- Miles traveled using public transportation on this day: " + element['publicmiles'] + " miles.")
							if element['ownmiles'] != '0':
								print("- Miles driven on their own vehicle on this day: " + element['ownmiles'] + " miles.")
							print(f'''- What their diet consisted of today: {element['diettype']}.
- Carbon dioxide emitted from food today: {element['carbondiet']} kilograms.
- Carbon dioxide emitted transportation today: {element['carbongas']} kilograms.
- Total carbon dioxide emitted today: {element['totalcarbon']} kilograms.''')
							break
					if found == True:
						break
					else:
						os.system('clear')
						date = input('''
The log was not found in your data!
You can make a day log in "Daily Logger".
Please enter the date you'd like to see.

Enter the date again (MM/DD/YYYY): ''') # telling user to correct the format of their date
						
			print('''
Would you like to view another log?

1) Yes
2) Go Back
''')
			choices = {"1","2"}
			choice = func.get_input(choices)

			if choice == 1:
				return 3
			else:
				return 0
		
		elif choice == 2:
			return 0

def friends_menu(currentuser):#dispaly the menu and allow the user to check friends activities
	os.system('clear')
	print('''
Here is where you can interact with your friends!

What would you like to do?
1) Friends' Activities
2) Add Friends
3) Check Pending Requests
4) Back to Main Menu
''')#print the menu
	choices = {"1","2","3","4"} #create a dictionary for choices
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
				os.system('clear')
				found2 = False
				for item in data:
					if item['userid'] == friendsID:
						print("\nHere's today's data for your friend, " + userfriendsname + ":\n" )
						found2 = True
						if item['publicmiles'] != '0':
							print("- Miles traveled using public transportation today: " + item['publicmiles'] + " miles.")
						if item['ownmiles'] != '0':
							print("- Miles driven on their own vehicle today: " + item['ownmiles'] + " miles.")
						print(f'''- What their diet consisted of today: {item['diettype']}.
- Carbon dioxide emitted from food today: {item['carbondiet']} kilograms.
- Carbon dioxide emitted transportation today: {item['carbongas']} kilograms.
- Total carbon dioxide emitted today: {item['totalcarbon']} kilograms.''')
				if found2 == False:
					print("Your friend has not logged their data today.")
				print('''
What would you like to do now?

1) Another User
2) Go Back
''')
				choices = {"1","2"}
				choice = func.get_input(choices)
				if choice == 2:
					return 0
				else:
					continue
			else:
				print('''
You are not friends with this user.
What would you like to do?

1) Another User
2) Go Back
''')
				choices = {"1","2"}
				choice = func.get_input(choices)
				if choice == 2:
					return 0
				else:
					continue
	if choice == 2: 
		choice = currentuser.add_friends()
		if choice == 0:
			return 0
	if choice == 3:
		choice = currentuser.pending_requests()
		if choice == 0:
			return 0
	if choice == 4:
		return 0