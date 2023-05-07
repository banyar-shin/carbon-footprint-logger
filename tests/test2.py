import csv

class UserAccount:
	__userid = "000006"
	__username = "aaronf"
	__password = "Aaron52@"
	__friends = list()
	__settings = dict()

	def save_user(self):
		file = open("csvfiles/users.csv", "a") # opening the users file
		to_write = "\n" + self.__userid + "," + self.__username + "," + self.__password # making a string for the user information
		file.write(to_write) # appending the userid, username, and password to file
		file.close() # closing the file
	
	def stay_signed_in(self):
		stay = input("Would you like to stay signed-in? (y/n): ") # asking user if they want to stay signed-in
		if stay.lower() == "y": # if the user says yes
			csv_headers = ['userid','username','password'] # setting the headers of the file
			userdata = {'userid': self.__userid, 'username': self.__username, 'password': self.__password} # setting the data that will be stored into the file
			with open("csvfiles/usersignedin.csv", 'w') as csvfile: # opening the users signed in file
				writer = csv.DictWriter(csvfile, fieldnames = csv_headers) # writing a csv file to the dictionary
				writer.writeheader() # writes the first row in the file as a header
				writer.writerow(userdata) # writes each inputted data into a row of the csv file

	def print_user(self):
		print(self.__userid, self.__username, self.__password)

currentuser = UserAccount()
currentuser.print_user()
currentuser.stay_signed_in()