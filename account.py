import csv

class UserSettings:
    __transtype = "\0"
    __housesize = 0
    

class UserAccount:
    __userID = "\0"
    __username = "\0"
    __password = "\0"
    __friends = set()

    def __init__(self, username, password, userID):
        self.__username = username
        self.__password = password
        self.__userID = userID

    def assignID(self):
        #opening file to access data
        file = open("users.csv", "r")
        data = list(csv.DictReader(file, delimiter=","))
        file.close()
        
        size = len(data)
        size += 1

        userid = str(size)
        zeroes_to_add = 6 - len(userid)

        zeroes = "0" * zeroes_to_add

        return (zeroes + userid)

    def set_password(input):
        password = input('''
        The password must contain at least a symbol and a number.
        Enter the password: 
        ''')
        # for element in password:
            

        

