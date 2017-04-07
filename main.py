#This is the main file of the program.

#Importing files which will be used in this program
from menu import *

#This is the main function of the program that actually starts it.
def main():
    menu = Menu()
    menu.welcome()
    menu.option()

#Calling the main function to launch the program
main()
