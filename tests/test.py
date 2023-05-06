import string #import string to use ascii sets for letter

def set_password(): #define the function
	letters = set(string.ascii_letters)#create the set for all alphabets
	upper = set(string.ascii_uppercase)#create the set for uppercase letters
	lower = set(string.ascii_lowercase)#create the set for lower letters
	numbers = {'0','1','2','3','4','5','6','7','8','9'} #create the set for numbers
	symbols = {'!','@','#','$','?','*','%','&','~','_'}#create the set for symbols
	password = input('''
Password Requirements:
- Must have at least 6 characters and at most 12 characters.
- Must include at least one letter, one number and one symbol.
Enter the password: ''')#Ask the user for input

	condition = "invalid" #set the condition for a while loop
	while condition == "invalid": #while the condition is invalid, start the loop
		if len(password) > 6 or len(password) < 12:#if the password length is greater 6 or less than 12
			upper_counter = 0 #initialize the uppercase counter
			lower_counter = 0 #initialize the lowercase counter
			number_counter = 0 #initialize the number counter
			for element in password: #read through each element in the password
				if element in upper: #if the element is the uppercase
					upper_counter += 1 #increment the uppercase counter
				if element in lower: #if the element is the lowercase
					lower_counter += 1 #increment the lowercase counter
				if element in numbers: #if the element is the number
					number_counter += 1 #increment the number counter
			if upper_counter >= 1 and lower_counter >= 1 and number_counter >= 1: #if there is an uppercase, lowercase and the number in the password
				base = pow(52,len(password)-2) * 62 * 72 #set the base 
				com = 1 #initialize the combination of the password
				for element in password: #read through every element in password
					if element in letters: #if the element is a letter
						com = com * 52 #com times 52
					if element in numbers: #if the element is a number
						com = com * 62 #com times 62
					if element in symbols: #if the element is a symbol
						com = com * 72 #com times 72
				if com >= base: #if com is greater than or equl to base
					condition = "valid" #set the condition to valid
		if condition == "invalid": #if the condition is invalid
			password = input('''
Password is not strong enough, please try again.
Enter the password: ''') #ask the user for input again
		elif condition == "valid": #else if the condition is valid
			print("You have successfully created a password!") #create the password
			return password #return the password

print(set_password())