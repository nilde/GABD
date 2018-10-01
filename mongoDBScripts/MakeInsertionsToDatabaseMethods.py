#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo

class InsertionMethodDatabase:
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

    def makeMethodsInsertions(self,methodsDescription,methodsData,client,DatabaseName):
        self.client=client
        methodsComplete={}
        for eachMethodData in methodsData:
            dataToInsert=eachMethodData[:3]
            dataToInsert.append(','.join(eachMethodData[3:]))
            print dataToInsert
            methodsComplete.update(dict(zip(methodsDescription,dataToInsert)))
            mydb = client[DatabaseName]
            mycol = mydb[configFile.METHOD_DATABASE]
            x = mycol.insert_one(methodsComplete)
            methodsComplete={}

            
        

