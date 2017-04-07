#This file is what will execute the main running of the program.

#Importing libraries/outside resources which will be used in the program
from pymongo import MongoClient

#Importing required files
from valid import *
from bathroom import *
from mongo import *
from menu import *

#This class will contain the methods that will run the heart of the program.
class Program():

    def base_menu(self, menu):
        print('\033c')
        bathroom = Bathroom()
        data = Database()
        print('1. Add Toilet Paper document')
        print('2. Update Toilet Paper levels')
        print('3. Check toilet paper amount in specific bathroom')
        print('4. Show bathrooms with a TP level above a specific amout')
        print('5. Show bathrooms with a TP level below a specific amout')
        choice = int(input('What is your choice '))
        if choice == 1:
            bathroom_selected = bathroom.bathroom_selection()
            tp_amount = bathroom.tp_amount()
            data.add(bathroom_selected, tp_amount)
            menu.option()
        elif choice == 2:
            bathroom_selected = bathroom.bathroom_selection()
            tp_amount = bathroom.tp_amount()
            data.update(bathroom_selected, tp_amount)
            menu.option()
        elif choice == 3:
            bathroom_selected = bathroom.bathroom_selection()
            bathroom_levels = data.find(bathroom_selected)
            for level in bathroom_levels:
                print(level)
            input('Press enter to continue ')
            menu.option()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
