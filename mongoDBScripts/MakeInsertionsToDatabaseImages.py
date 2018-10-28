#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo
import gridfs
import pickle
from bson.binary import Binary
import numpy as np
import json

class InsertionImagesDatabase:
    def __init__(self):
        self.imagesNames=[]
        self.imagesAllValues=[]
        self.client=object()

    def setValues(self,imagesNames,imagesAllValues):
        self.imagesNames=imagesNames
        self.imagesAllValues=imagesAllValues

    def insertSections(self,allSections,DatabaseName,client):
        
        dataSection={}
        for eachSection in allSections:
            for i,section in enumerate(eachSection):
                dataSection['Section_'+str(i+1)]=section[0]
        mydb = client[DatabaseName]
        mycol = mydb[configFile.COLLECTIONS_NAMES[0]]
        x = mycol.insert_one(dataSection)

    def makeImagesInsertions(self,allNetsInformation,allNetsData,allClassesInformation,allVectorsInformation,client,DatabaseName):
        self.client=client
        mydb = client[DatabaseName]
        #USAR EL COMANDO DE COMMAND PARA GESTIONAR LA PETICION A LA BASE DE DATOS Y NO USAR ESTO QUE NO FUNCIONA
        #BASARSE EN EL YA CREADO ANTERIORMETNE
        #client.VECT.command('usersInfo')
        #mydb.settings.save( { _id:"chunksize", value: 1024 } )

        '''
        Reescribir comando, mirar el equivalente en pymongo para update settings
        self.client[DatabaseName].command("updateSettings",
            {'chunkSize':1024})
        '''
        mycol = mydb[configFile.IMAGE_DATABASE]
    
        #fs = gridfs.GridFS(mydb)
        
        #indexClasses = fs.put(Binary(pickle.dumps(allClassesInformation, protocol=2)))
        imagesComplete={}
        for i,eachNetData in enumerate(allNetsData):
            imagesComplete.update(dict(zip(allNetsInformation[:2],eachNetData[:2])))
            imagesComplete['classes']=allClassesInformation
            #FUERA
            #indexVectors = fs.put(Binary(pickle.dumps(allVectorsInformation[i], protocol=2)))
            #imagesComplete['vectors']=json.dumps(allVectorsInformation[:])
            #x = mycol.insert_one(imagesComplete)
            imagesComplete={}


