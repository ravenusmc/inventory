#This file will hold all of the validation functions for the program

def option_valid(choice):
    if choice < 1 or choice > 3:
        return False
    else:
        return True

def valid_bathroom(choice):
    if choice < 1 or choice > 4:
        return False
    else:
        return True

def tp_amount_valid(tp_amount):
    if tp_amount >= 0:
        return True
