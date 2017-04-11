#This is the main file of the program.

#Importing files which will be used in this program
from menu import *
from create import *
from login import *

#This is the main function of the program that actually starts it.
def main():
    create = Create()
    login = Login()
    password = create.encrypt_pass()
    login.insert_admin(password)
    menu = Menu()
    menu.welcome()
    menu.option()

#Calling the main function to launch the program
main()
