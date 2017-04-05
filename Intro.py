#This file will hold the class that will introduce the user to the program.

#Importing files which will be used
from valid import *
from support import *

#This class will contain methods that deal with the basic running of the program
class Intro():

    #This method will great the user
    def welcome(self):
        print('\033c')
        print('------------------------------')
        print('Welcome to TP Inventory System')
        print('------Tracking TP usage------')
        print('------------------------------')
        input('Press enter to continue ')

    #This method will allow the user to choose which option they want to do.
    def option(self):
        print('\033c')
        support = Support()
        intro = Intro()
        print('1. Use Program')
        print('2. Help')
        print('3. Quit')
        choice = int(input('What is your choice? '))
        while not option_valid(choice):
            print('That was not a valid selection')
            choice = int(input('What is your choice? '))
        if choice == 1:
            pass
        elif choice == 2:
            support.help()
            intro.option()
        elif choice == 3:
            support.quit()
