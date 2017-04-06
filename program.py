#This file is what will execute the main running of the program.

#Importing libraries/outside resources which will be used in the program
from pymongo import MongoClient

#Importing required files
from valid import *
from bathroom import *
from mongo import *

#This class will contain the methods that will run the heart of the program.
class Program():

    def base_menu(self):
        print('\033c')
        bathroom = Bathroom()
        data = Database()
        print('1. Add Toilet Paper')
        print('2. Delete Toilet Paper')
        print('3. Check toilet paper amount')
        choice = int(input('What is your choice '))
        if choice == 1:
            bathroom_selected = bathroom.bathroom_selection()
            tp_amount = bathroom.tp_amount()
            data.add(bathroom_selected, tp_amount)
        elif choice == 2:
            bathroom_selected = bathroom.bathroom_selection()
        elif choice == 3:
            pass
