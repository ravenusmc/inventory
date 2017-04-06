#This file will hold the class for connecting to the Mongo DB.

#Importing files which will be used in the program
from pymongo import MongoClient

class Database():

    def database_setup(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        db = self.client.inventory #Creating the inventory DB
        #coll = db.paper #Creating a paper collection within the inventory DB
        db.paper
        db.paper.insert_one({
            "bathroom_desc": 1,
            "tp": 3
        })
        print('done!')
        #return coll

data = Database()
data.database_setup()

# db.users.insert_one({
#   "first_name": "Test",
#   "last_name": "Me",
#   "user": "TestMe",
#   "password": "pass"
# )}

# client = MongoClient()
# db = client.titanic
# db.users
# db.users.insert_one({
#     "first_name": "Test",
#     "last_name": "Me",
#     "user": "TestMe",
#     "password": "pass"

# })
