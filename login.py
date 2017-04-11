#This file will contain the methods to allow a user to actually log into the
#program.

#Importing files which will be used in the program
from pymongo import MongoClient

class Login():

    def __init__(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        self.db = self.client.user #Creating the users collection
        self.db.users = self.db.users

    #This method will insert the admin user into the program. In a real world
    #program I would have the password better hidden. See the create class.
    def insert_admin(self, password):
        self.db.users.insert_one({
            "username": "admin",
            "password": password
        })
