#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo
import re

class InsertionExperimentsDatabase:
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

    def makeExperimentsInsertions(self,methodsDescription,methodsData,client,DatabaseName):
        self.client=client
        mydb = client[DatabaseName]
        mycol = mydb[configFile.EXPERIMENTS_DATABASE]
        methodsComplete={}
        counter=[]
        for eachMethodData in methodsData:
            #Is used for find the first closing brackets that causes problems in the correct insertion of the data
            for i,part in enumerate(eachMethodData):
                if ']' in part:
                    counter.append(i)
            print counter
            dataToInsert=[]
            preparedData=eachMethodData[:counter[0]+1]
            preparedData[0]=preparedData[0][1:]
            preparedData[-1]=preparedData[-1][:-1]
            dataToInsert.append({'values':preparedData})

            dataToInsert.append(eachMethodData[counter[0]+1][:])

            preparedData=eachMethodData[counter[0]+2:counter[1]+1]
            preparedData[0]=preparedData[0][1:]
            preparedData[-1]=preparedData[-1][:-1]
            openBrackets=[]
            closeBrackets=[]
            finishArray=[]
            for index,char in preparedData:
                if char=='{':
                    openBrackets.append(index)
                else
                    if char=='}':
                        closeBrackets.append(index)
            
            dataToInsert.append({'values':','.join(preparedData)})

            preparedData=eachMethodData[counter[1]+1:]
            preparedData[0]=preparedData[0][1:]
            preparedData[-1]=preparedData[-1][:-1]

            dataToInsert.append({'values':preparedData})
            print dataToInsert
            raw_input("x")
            methodsComplete.update(dict(zip(methodsDescription,dataToInsert)))
            x = mycol.insert_one(methodsComplete)
            methodsComplete={}
            counter=[]
