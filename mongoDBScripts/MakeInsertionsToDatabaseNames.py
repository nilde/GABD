#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo
import gridfs
from bson.binary import Binary
import pickle


def insertSections(allSections,allClasses,DatabaseName,client,dataVectors):
    dataSection={}
    vectorBufferComplete=[]
    mydb = client[DatabaseName]
    mycol = mydb[configFile.COLLECTIONS_NAMES[0]]
    #Eliminacion del gridfs en favor de un aumento del chunk (Por hacer)
    fs = gridfs.GridFS(mydb)
    for j,eachClass in enumerate(allClasses):
        dataSection={}
        dataSection['name']=eachClass
        for i,eachSection in enumerate(allSections[j]):
            dataSection[configFile.VECTOR_FILENAMES_SECTIONS[i]]=eachSection[0]
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

