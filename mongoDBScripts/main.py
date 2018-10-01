#!/usr/bin/python

#Contains all imports needed to resolve the dependencies
import sys

import configFile 
import ExtractDataNames
from ExtractDataData import extractData
from ExtractDataMethods import ExtractMethods
import ExtractDataMethods
import MakeDatabase
import MakeInsertionsToDatabaseNames
import MakeInsertionsToDatabaseData
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
    methodExtractor=ExtractMethods()
   
    print 'Parametros: '
    if len(sys.argv)==0:
        print 'No se han introducido parametros'

    if DropDatabaseConstant in sys.argv:
        DropDatabase=True
        print '--drop : Cuidado, has escogido la opcion drop espero que sepas lo que estas haciendo...'

    if DatabaseNameConstant in sys.argv:
        DatabaseName=sys.argv[-1]
        print '--db : Has introducido un nombre para la base de datos diferente\n'

    print "FASE 1: Configuracion de la base de datos: " 
    serverStatus,client=MakeDatabase.createDatabase(DropDatabase,DatabaseName)
    if not serverStatus:
        return -1


    methodExtractor.extractAllMethodInformation()
    print "FASE 2: Extraccion de las fases: "   
    allSections,allData=ExtractDataNames.main()
    MakeInsertionsToDatabaseNames.insertSections(allSections,DatabaseName,client)
    mydb = client[configFile.DATABASE_NAME]
    mycol = mydb[configFile.COLLECTIONS_NAMES[0]]
    print "FASE 3: Extraccion de los datos: "
    allClasses,allData=dataExtractor.makeExtraction()
    print allData
    time.sleep(0.5)
    print "FASE 4: Insercion de los datos: "
    MakeInsertionsToDatabaseData.insertData(allData,allClasses,DatabaseName)


    #Delete of the element that mantains open the connection

    mycol.delete_one({'TEST': 'TEST'})

    print 'EJECUCION COMPLETA SIN ERRORES :)'
    
    clientConsole.start(client)

if __name__=="__main__":
    main()
