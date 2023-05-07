import csv
import datetime
import os

def get_int():
    x = input("Enter an integer: ") # ask user for input
    while True: # while there is input,
        try:  # try this line
            int(x)  # check if input is integer
        except ValueError: # if there is type error,
            print("\033[A\033[A")
            x = input("Invalid, only enter an integer: ") # ask for input again
        else: # if not,
            return int(x)  # return the input
	
def get_input(choices):
    choice = input("Enter a number: ")
    while True:
        if choice in choices:
            return int(choice)
        else:
            print("\033[A\033[A")
            choice = input("Invalid Input. Please re-enter: ")

class UserAccount:
	__userid = "000001"
	__username = "banyar"
	__password = "Banyar123"
	__friends = list()
	__outgoing = list()
	__incoming = list()
	__settings = {
		'userid': '000001',
		'public': '1',
		'savedvehicle': '25',
		'household': '3',
		'recycle': '1'
	}

	def get_userid(self):
		return self.__userid


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

	mysettings = {
		'userid': '000001',
		'public': '1',
		'savedvehicle': '25',
		'household': '3',
		'recycle': '1'
	}
	
	if mysettings['public'] == '1':
		os.system('clear')
		print(f'''
The date is set to {date}.
Please provide how many miles you traveled using
public transportation on this day.
''')
		publicmiles = get_int()
	else: 
		publicmiles = 0
	
	if mysettings['savedvehicle'] != 'none':
		os.system('clear')
		print(f'''
The date is set to {date}.
Please provide how many miles you traveled using
your saved vehicle on this day.
''')
		privatemiles = get_int()
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
	diet = get_input(choices)

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