#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo
import sys

def insertData(allData,allClasses,DatabaseName):
    print ' Insercion de los vectores en proceso'
    dataEachVector={}
    client = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
    mydb = client[DatabaseName]
    mycol = mydb[configFile.COLLECTIONS_NAMES[2]]

    counter=0
    for indexSet,setOfVectors in enumerate(allData):
        for vector in setOfVectors:
            dataEachVector['database']=allClasses[indexSet]
            dataEachVector['class']=allClasses[indexSet][-1]
            dataEachVector['vector']=vector
            
            mycol.insert_one(dataEachVector)
            dataEachVector={}
            counter+=1
            if counter%1000==0:
                
                sys.stdout.write('.')
                sys.stdout.flush()
    
    sys.stdout.flush()
    CURSOR_UP_ONE = '\x1b[1A'            
    ERASE_LINE = '\x1b[2K'
    for i in range(3):
        print '%s\r' % ''*20, # clean up row
        print '', # note ending with comma
    print 'Insercion de los vectores terminada'
    print '//////////////////////////////////////////////////////////\n'
