import os
import func

loop = "y"

while loop == "y":
    choice = func.home_page()
    if choice == 1:
        func.general_info()
    elif choice == 2:
        cf, loop = func.cal_carbon_footprint()
    elif choice == 3:
        func.general_tips()
    elif choice == 4:
        break

print("Thank you for using our program!!")