#This file will contain the methods to allow a user to actually log into the
#program.

#Importing files which will be used in the program
from pymongo import MongoClient
import bcrypt

#importing my own files for the project
from valid import *

#This class will deal with the logging in of users as well as dealing with the admin role
class Login():

    def __init__(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        self.db = self.client.user #Creating the users collection
        self.db.users = self.db.users

    #This method will insert the admin user into the program. In a real world
    #program I would have the password better hidden. See the create class.
    def insert_admin(self, password):
        check_admin = self.db.users.find_one({
            "username": "admin",
        });
        if str(check_admin) == 'None':
            self.db.users.insert_one({
                "username": "admin",
                "password": password
            })
        #Code here was for my own reference. It is not needed in the final product.
        # else:
        #     print('Admin is present in DB')
        #     input('Press Enter')

    #This method will allow the user to log into the program.
    def login_screen(self, password, hashed):
        print('\033c')
        print('------------')
        print('Login Screen')
        print('------------')
        print()
        print('1. Yes, I have an account')
        print('2. No, I don\'t have an account')
        choice = int(input('Do you have an account? (1/2) '))
        while not login_valid(choice):
            print('That was not a valid selection!')
            choice = int(input('Do you have an account? (1/2) '))
        if choice == 1:
            username = input('Please enter your username: ')
            password = input('Please enter your password: ')
            return username, password
        elif choice == 2:
            username, password = self.create_account(password, hashed)
            return username, password

    #This method will see if the username and password are in the database.
    def check(self, username, password):
        user_real = self.db.users.find_one({
            "username": username,
            "password": password
        });
        if str(user_real) == 'None':
            flag = False
        else:
            flag = True
        return flag

    #This method will allow the user to create an account
    def create_account(self, password, hashed):
        print('\033c')
        admin_password = input('Please enter the admin password: ')
        admin_password = admin_password.encode('utf-8')
        if bcrypt.hashpw(admin_password, hashed) == hashed:
            username = input('Please enter your username: ')
            password = input('Please enter your password: ')
            self.db.users.insert_one({
                "username": username,
                "password": password
            })
            return username, password
        else:
            print('Sorry the Admin password was wrong!!!')
            input('Press enter to continue and face the consequences!')
            username = 'fake'
            password = 'fake'
            return username, password


    #### THE BELOW IS KEPT ONLY FOR REFERENCE #######
    #This was the old create_account I ran into way to many problems doing it this
    #way and ended up with way short code above!!!!
    # def create_account(self, password, hashed):
    #     print('\033c')
    #     admin_password = input('Please enter the admin password: ')
    #     admin_password = admin_password.encode('utf-8')
    #     if bcrypt.hashpw(admin_password, hashed) == hashed:
    #       print('it matches!')
    #       input('enter')
    #     else:
    #       print('no match')
    #       input('enter')
    #     admin = self.db.users.find_one({
    #         "username": "admin",
    #         "password": admin_password
    #     });
    #     check_admin = self.db.users.find_one({
    #         "username": "admin",
    #         "password": admin_password
    #     });
    #     input('Enter to continue')
    #     if str(check_admin) == 'None':
    #         print('Sorry the Admin password was wrong!!!')
    #         input('Press enter to continue and face the consequences!')
    #         username = 'fake'
    #         password = 'fake'
    #         return username, password
    #     else:
    #         username = input('Please enter your username: ')
    #         password = input('Please enter your password: ')
    #         self.db.users.insert_one({
    #             "username": username,
    #             "password": password
    #         })
    #         return username, password
