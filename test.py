import string
letters = set(string.ascii_letters)
numbers = {'0','1','2','3','4','5','6','7','8','9'}
symbols = {'!','@','#','$','?','*','%','&','~','_'}

def set_password(input):
	com = 1
	alpha_counter = 0
	num_counter = 0
	sym_counter = 0
	password = input('''The password must contain at least a symbol and a number.
	Enter the password: ''')
	while len(password) < 6 or len(password) > 12:
		password = input('''The password must have at least 6 characters and at most 12 characters
		Enter the password again: ''')
		base = pow(52,len(password)-2) * 62 * 72
		for element in password:
			if element in letters:
				com = com * 52
				alpha_counter += 1
			if element in numbers:
				com = com * 62
				num_counter += 1
			if element in symbols:
				com = com * 72
				sym_counter += 1
		if alpha_counter > 1 or num_counter > 1 or sym_counter > 1 or com >= base:
			print("You have successfully created the password.")

set_password(input)
