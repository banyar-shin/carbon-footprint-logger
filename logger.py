from account import UserAccount
import csv
import func

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

    if userinput == 1:
        return 1
    if userinput == 2:
        return 2
    if userinput == 3:
        return 3