import string
letters = set(string.ascii_letters)
numbers = set(range(0,10))
symbols = {'!','@','#','$','?','*','%','&','~','_'}

print(numbers)

#set the function for password validation
def set_password(input):
  #ask the user for input
  password = input('''
  The password must contain at least a symbol and a number.
  Enter the password: 
  ''')
  #read through each character 
  #for element in password:
    #check the length is greater than 6 and less than 12
    
