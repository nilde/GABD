#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo
import sys
import gridfs
from bson.binary import Binary
import pickle

def insertData(allData,allClasses,DatabaseName):
    print ' Insercion de los vectores en proceso'
    dataEachVector={}
    client = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
    mydb = client[DatabaseName]
    mycol = mydb[configFile.COLLECTIONS_NAMES[2]]
    fs = gridfs.GridFS(mydb)
    for indexSet,setOfVectors in enumerate(allData):
        dataEachVector['database']=allClasses[indexSet]
        dataEachVector['class']=allClasses[indexSet][-1]
        indexVectors = fs.put(Binary(pickle.dumps(setOfVectors, protocol=2)))
        dataEachVector['vector']=indexVectors
            
        mycol.insert_one(dataEachVector)
        dataEachVector={}
    print 'Insercion de los vectores terminada'
    print '//////////////////////////////////////////////////////////\n'
