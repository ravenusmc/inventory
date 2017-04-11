#This file will hold the class for connecting to the Mongo DB.

#Importing files which will be used in the program
from pymongo import MongoClient

#This class will hold all the methods for using the TP collection.
class Database():

    def __init__(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        self.db = self.client.inventory #Creating the inventory collection
        self.db.paper = self.db.paper

    #This method will add a new document to the database.
    def add(self, bathroom, tp):
        self.db.paper.insert_one({
            "bathroom_desc": bathroom,
            "tp": tp
        })

    #This method will the user to update a record.
    def update(self, bathroom, tp):
        self.db.paper.update_one(
            { "bathroom_desc": bathroom },
            {
                "$set":{
                    "tp": tp
            },
        })

    #This method will allow the user to see how many tp rolls are in a specific
    #bathroom
    def find(self, bathroom):
        bathroom_levels = self.db.paper.find({
            "bathroom_desc": bathroom
        })
        return bathroom_levels

    #This method will allow the user to find which bathrooms have a certain number
    #of tp rolls above a certain number.
    def find_specific_gt(self, tp):
        bathroom_levels = self.db.paper.find({
            "tp": {"$gt": tp }
        })
        return bathroom_levels

    #This method will allow the user to find which bathrooms have a certain number
    #of tp rolls below a certain number.
    def find_specific_lt(self, tp):
        bathroom_levels = self.db.paper.find({
            "tp": {"$lt": tp }
        })
        return bathroom_levels
