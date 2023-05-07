import os
import time
from account import UserAccount
import logger

def get_input(choices):
    choice = input("Enter a number: ")
    while True:
        if choice in choices:
            return int(choice)
        else:
            print("\033[A\033[A")
            choice = input("Invalid Input. Please re-enter: ")

def greet_user():
    os.system('clear')
    print('''
BAM!!! Welcome to Carbon Logger! This program allows you to track your carbon footprint, depending on the activites you perform on 
a daily basis. You will also be given the ability to adjust your circumstances accordingly, whether it is the situation with your 
household or transportation. Every month, you can keep track of your monthly bills and the number of hours spent flying an airplane.

What would you like to do?
1) Our Purpose
2) Carbon Logger
3) Quit
''')
    choices = {"1","2","3"}
    choice = get_input(choices)
    return choice

def our_purpose():
    os.system('clear')
    print('''
    The amount of carbon dioxide we put into the atmosphere directly affects and worsens climate change. It is a type of gas
that is able to trap heat, engendering our planet to warm up. One of the main driving forces of these greenhouse gases is the 
burning of fossil fuels, which is used towards transportation, the production of electricity, and the powering industries and our 
homes, etc. Despite the use of fossil fuels providing us with advantages and giving more people jobs, the immense quantities of 
carbon emissions that it produces is ultimately killing our planet.

    With our concern of the evergrowing problem of carbon emissions, we have decided to create a program that spreads awareness 
of the issue and allows users to keep track of how much carbon dioxide that they are responsible for generating. By answering
our daily questions, the user is able to find out their carbon footprint each day. In order to create a positive impact, there
are small habits to develop that can be greatly beneficial.

    There are various ways and adjustments you can make in your daily life to help the environment. For instance, one of the
highest contributing factors of human behavior that is responsible for carbon emissions is transportation. To alleviate this, it
would help to carpool if you and at least one other person (friends, family members, coworkers, etc.) are going to the same 
destination, or you can try out public transportation. If you find that your monthly electricity and water bills come out pretty 
high, it would be great to focus on taking shorter showers, unplugging chargers and cords that aren't in use, switching to more
energy efficient bulbs, line dry your laundry, etc.

What would you like to do?
1) Main Menu
2) Quit
''')
    choices = {"1","2"}
    userinput = get_input(choices)
    
    if userinput == 1:
        choice = 0
    else:
        choice = 3

    return choice

def quit_program():
    os.system('clear')
    print('''
Thank you for using Carbon Logger!!
Please come again!!
''')

def carbon_logger():
    os.system('clear')
    currentuser = UserAccount()

    signedin = logger.signed_in()
    if signedin == True:
        userid, username, password = logger.read_in_user()
        currentuser.set_user(userid, username, password)
    else:
        choice2 = logger.login_or_signup()
        if choice2 == 1:
            currentuser.login_username()
            currentuser.login_password()
            currentuser.get_friends()
        elif choice2 == 2:
            currentuser.signup_username()
            currentuser.signup_password()
            currentuser.assignID()
            currentuser.save_user()
            return 3
        elif choice2 == 3:
            return choice2

def main_menu(choice):
    while True:
        if choice == 0:
            choice = greet_user()
        elif choice == 1:
            choice = our_purpose()
        elif choice == 2:
            choice = carbon_logger()
        elif choice == 3:
            quit_program()
            break