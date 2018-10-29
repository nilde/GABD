#!/usr/bin/python

#Contains all imports needed to resolve the dependencies
import sys

import configFile 
import ExtractDataNames
from ExtractDataData import extractData
from ExtractDataResults import ExtractFromFile
from ExtractDataImages import ExtractFromImagesFiles
import MakeDatabase
import MakeInsertionsToDatabaseNames
import MakeInsertionsToDatabaseData
from MakeInsertionsUsers import InsertionUsers
from MakeInsertionsToDatabaseResults import InsertionResultDatabase
from MakeInsertionsToDatabaseMethods import InsertionMethodDatabase
from MakeInsertionsToDatabaseImages import InsertionImagesDatabase
from Client import ClientConsole
import pymongo
from bson.objectid import ObjectId

import argparse
import os 
import platform
import time

#CONSTANTS
DropDatabase=False
DropDatabaseConstant='--drop'
DatabaseNameConstant='--db'
DatabaseName=configFile.DATABASE_NAME

#TEMPORAL BUFFER FOR MORE INFORMATION
more=False

#Argparse help
parser=argparse.ArgumentParser(
    description='''Script que permite la insercion automatica de todos los datos de las diferentes fuentes de datos en una base de datos mongoDB''',
    epilog="""TODAVIA EN CONSTRUCCION""")
parser.add_argument('--drop',nargs=1,help='Si se introduce esta opcion se vaciara el contenido de la base de datos antes de introducir el nuevo contenido')
parser.add_argument('--db',nargs=2,help='Indicar un nombre concreto para la base de datos y no el del archivo de configuracion')

def main():
    clientConsole=ClientConsole()
    dataExtractor=extractData()
    dataExtractor_N=ExtractFromFile()
    dataExtractor_I=ExtractFromImagesFiles()
    methodInsertion=InsertionMethodDatabase()
    imagesInsertion=InsertionImagesDatabase()
    resultsInsertion=InsertionResultDatabase()
    
   
    print 'Parametros: '
    if len(sys.argv)==0:
        print 'No se han introducido parametros'

    if DropDatabaseConstant in sys.argv:
        DropDatabase=True
        print '--drop : Cuidado, has escogido la opcion drop espero que sepas lo que estas haciendo ...'

    if DatabaseNameConstant in sys.argv:
        DatabaseName=sys.argv[-1]
        print '--db : Has introducido un nombre para la base de datos diferente\n'

    print "FASE 1: Configuracion de la base de datos: " 
    serverStatus,client=MakeDatabase.createDatabase(DropDatabase,DatabaseName)
    if not serverStatus:
        return -1


    
    print "FASE 2: Extraccion de las fases "

    print "FASE 3: Extraccion de los datos "
    allClasses,allData=dataExtractor.makeExtraction()
    allSections,allDataV=ExtractDataNames.main()

    allNetsDescription,allNetsData,allClassesImages,allDataVectorsImages=dataExtractor_I.makeExtraction()
    imagesInsertion.makeImagesInsertions(allNetsDescription,allNetsData,allClassesImages,allDataVectorsImages,client,DatabaseName)
    
    print "FASE 4: Insercion de los datos"
    MakeInsertionsToDatabaseNames.insertSections(allSections,allClasses,DatabaseName,client,allDataV)
    
    print "FASE 5: Insercion de los metodos"
    description,data=dataExtractor_N.makeExtraction(configFile.METHOD_PATH,configFile.METHOD_FILENAME_NAMES,configFile.METHOD_FILENAME_DATA)
    methodInsertion.makeMethodsInsertions(description,data,client,DatabaseName)
    del description[:]
    del data[:]

    print "FASE 6: Insercion de los resultados"
    description,data=dataExtractor_N.makeExtraction(configFile.RESULT_PATH,configFile.RESULT_FILENAME_NAMES,configFile.RESULT_FILENAME_DATA) 
    resultsInsertion.makeResultsInsertions(description,data,client,DatabaseName)
    del description[:]
    del data[:]


    print 'EJECUCION COMPLETA SIN ERRORES :)'
    usersInsertion=InsertionUsers(client)
    clientConsole.start(client)
    #client.drop_database(DatabaseName)
    client.close()


    

if __name__=="__main__":
    main()
