#This is the main file of the program.

#Importing files which will be used in this program
from menu import *
from create import *
from login import *

#This is the main function of the program that actually starts it.
def main():
    #creating objects
    create = Create()
    login = Login()
    menu = Menu()
    menu.welcome()
    #encrptying admin password
    password, hashed = create.encrypt_pass()
    #Creating an admin account in the database
    login.insert_admin(hashed)
    #allowing the user to log in.
    username, password = login.login_screen(password, hashed)
    #checking to see if the username and password match.
    flag = login.check(username, password)
    #Here I use a conditional statement to test whether the program has an intruder or
    #not. 
    if flag == False:
        intruder()
    else:
        menu.option()

#This function will be called if the user enters the wrong username and password
def intruder():
    print('\033c')
    print('You are an intruder and not supposed to be using this program!!!')
    print('The authorities have been notified!!!')
    print('Leave now!')
    input('Press enter to close the program and save your soul!!!')

#Calling the main function to launch the program
main()
