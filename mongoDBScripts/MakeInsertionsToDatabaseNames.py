#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo

def insertSections(allSections,DatabaseName):
    dataSection={}
    for eachSection in allSections:
        for i,section in enumerate(eachSection):
            dataSection['Section_'+str(i+1)]=section[0]
    
    client = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
    mydb = client[DatabaseName]
    mycol = mydb[configFile.COLLECTIONS_NAMES[0]]
    x = mycol.insert_one(dataSection)
