import os
import time

def mul(x, y):
    z = x * y
    return z

def new_user():
    ans = input("Are you a new user? (y/n): ")

def cal_carbon_footprint():
    ELECGAS = 105
    OIL = 113
    MILE = 0.79
    FLIGHT1 = 1100
    FLIGHT2 = 4400
    RECYNEWS = 184
    RECYALU = 166

    total = 0

    ebill = int(input("What is your monthly electric bill (nearest dollar)? "))
    total += mul(ebill, ELECGAS)

    gbill = int(input("What is your monthly gas bill (nearest dollar)? "))
    total += mul(gbill, ELECGAS)

    obill = int(input("What is your monthly oil bill (nearest dollar)? "))
    total += mul(obill, OIL)

    mbill = int(input("What is your yearly mileage (nearest mile)? "))
    total += mul(mbill, MILE)

    f1bill = int(input("How many flights have you taken in the past year (4 hours or less)? "))
    total += mul(f1bill, FLIGHT1)

    f2bill = int(input("How many flights have you taken in the past year (4 hours or more)? "))
    total += mul(f2bill, FLIGHT2)

    recypaper = int(input("Enter 1 if you recycle the newspaper: "))
    if recypaper == 1:
        total += RECYNEWS

    recyalu = int(input("Enter 1 if you recycle aluminum and tin: "))
    if recyalu == 1:
        total += RECYALU

    print("Your carbon footprint:", total)

    choice = input("Would you like to return to the home page? (y/n) ")

    print("Sending you back...")
    time.sleep(2)
    os.system('clear')

    return total, choice

def general_info():
    print("Sorry! This page is still under construction.")
    
    print("Sending you back...")
    time.sleep(2)
    os.system('clear')

def general_tips():
    print("Sorry! This page is still under construction.")
    
    print("Sending you back...")
    time.sleep(2)
    os.system('clear')

def home_page():
    choice = int(input('''
    Hello! What do you want to do?
    1) Login (Existing User)
    2) Sign-Up (New User)
    3) General Information
    4) General Tips
    5) Quit
    Enter a number: '''))

    os.system('clear')
    
    return choice