#This file will hold all of the validation functions for the program

def option_valid(choice):
    if choice < 1 or choice > 3:
        return False
    else:
        return True 
