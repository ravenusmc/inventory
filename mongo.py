#This file will hold the class for connecting to the Mongo DB.

#Importing files which will be used in the program
from pymongo import MongoClient

#This class will hold all the methods for using the database.
class Database():

    def __init__(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        self.db = self.client.inventory #Creating the inventory DB
        self.db.paper = self.db.paper

    def add(self, bathroom, tp):
        self.db.paper.insert_one({
            "bathroom_desc": bathroom,
            "tp": tp
        })
        print('done!')

# data = Database()
# data.add()
