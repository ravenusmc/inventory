#This file is what will execute the main running of the program.

#Importing required files
from valid import *
from bathroom import *

#This class will contain the methods that will run the heart of the program.
class Program():

    def base_menu(self):
        print('\033c')
        bathroom = Bathroom()
        print('1. Add Toilet Paper')
        print('2. Delete Toilet Paper')
        print('3. Check toilet paper amount')
        choice = int(input('What is your choice '))
        if choice == 1:
            bathroom_selected = bathroom.bathroom_selection()    
        elif choice == 2:
            bathroom_selected = bathroom.bathroom_selection()
        elif choice == 3:
            pass
