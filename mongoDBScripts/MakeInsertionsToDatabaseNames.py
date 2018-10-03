#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo

def insertSections(allSections,allClasses,DatabaseName,client,dataVectors):
    dataSection={}
    vectorBufferComplete=[]
    mydb = client[DatabaseName]
    mycol = mydb[configFile.COLLECTIONS_NAMES[0]]
    for j,eachClass in enumerate(allClasses):
        dataSection={}
        dataSection['name']=eachClass
        for eachSection in allSections:
            for i,section in enumerate(eachSection):
                dataSection[configFile.VECTOR_FILENAMES_SECTIONS[i]]=section[0]

        vectorBuffer={}
        vectorBufferComplete=[]
        for eachVector in dataVectors[j]:
            if len(eachVector)>0:
                vectorBuffer['class']=eachVector[-1]
                vectorBuffer['vector']=eachVector
                vectorBufferComplete.append(vectorBuffer)
                vectorBuffer={}
        dataSection['content']=vectorBufferComplete
        mycol.insert_one(dataSection)
    
