#This file will hold the bathroom class

#importing files which will be used in this program
from valid import *

#This class will hold all of the methods for allowing the user to select which
#bathroom they want to work with.
class Bathroom():

    #This method will allow the user to select the bathroom
    def bathroom_selection(self):
        print('\033c')
        print('1. Master Bathroom')
        print('2. Upstairs Bathroom')
        print('3. Main Level Bathroom')
        print('4. Basement Bathroom')
        choice = int(input('What is your selection: '))
        while not valid_bathroom(choice):
            print('What was not a valid choice!')
            choice = int(input('What is your selection: '))
        if choice == 1:
            return 'Master_Bathroom'
        elif choice == 2:
            return 'Upstairs_Bathroom'
        elif choice == 3:
            return 'Main_level_Bathroom'
        elif choice == 4:
            return 'Basement_Bathroom'

    #This method will allow the user to select the amount of toilet paper.
    def tp_amount(self):
        print('\033c')
        tp_amount = int(input('Please enter the number of tp rolls counted: '))
        while not tp_amount_valid(tp_amount):
            print('That is not a valid selection!')
            tp_amount = int(input('Please enter the number of tp rolls counted: '))
        return tp_amount
