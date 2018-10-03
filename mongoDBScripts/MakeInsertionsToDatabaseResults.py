#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo

class InsertionResultDatabase:
    def __init__(self):
        self.methodsNames=[]
        self.methodsAllValues=[]
        self.client=object()

    def setValues(self,methodsNames,methodsAllValues):
        self.methodsNames=methodsNames
        self.methodsAllValues=methodsAllValues

    def insertSections(self,allSections,DatabaseName,client):
        
        dataSection={}
        for eachSection in allSections:
            for i,section in enumerate(eachSection):
                dataSection['Section_'+str(i+1)]=section[0]
        mydb = client[DatabaseName]
        mycol = mydb[configFile.COLLECTIONS_NAMES[0]]
        x = mycol.insert_one(dataSection)

    def makeResultsInsertions(self,resultsDescription,resultsData,client,DatabaseName):
        self.client=client
        resultsComplete={}
        for eachResultData in resultsData:
            dataToInsert=eachResultData
            resultsComplete.update(dict(zip(resultsDescription,dataToInsert)))
            mydb = client[DatabaseName]
            mycol = mydb[configFile.RESULT_DATABASE]
            x = mycol.insert_one(resultsComplete)
            resultsComplete={}

            
        

