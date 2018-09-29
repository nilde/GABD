#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import ExtractDataNames
import ExtractDataData
import MakeDatabase
import MakeInsertionsToDatabaseNames
import MakeInsertionsToDatabaseData
import pymongo
from bson.objectid import ObjectId
import sys
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

def printLogo():
    print "\n"
    print "     xxxxxxxxxxxxxxxxxxxxxxx     " 
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    print "   ___     ___     ___     ___  " 
    print " /  __|   /   \   | _ )   |   \  "
    print " | (_ |   | - |   | _ \   | |) | "
    print "  \___|   |_|_|   |___/   |___/  "
    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    print "     xxxxxxxxxxxxxxxxxxxxxxx     \n\n" 

def printOptions():
    print 'Introduce "quit" para cerrar la sesion'
    print 'Introduce "addDB" para introducir una base de de datos'
    print 'Introduce "add" para introducir un nuevo elemento en alguna coleccion'
    print 'Introduce "info" para obtener la informacion de la BD'
    print 'Introduce "more" para obtener la lista completa de comandos'
    print 'Introduce "dropbd" para eliminar una base de datos'
    print 'Introduce "dropcol" para eliminar una coleccion'
    print '----------------------------------------------------------\nCONSOLA:\n'

def refreshScreen():
    if platform.system=='Windows':
        os.system('cls')
    else:
        os.system('clear')
    printLogo()
    printOptions()

def gestionateAddDB():
    refreshScreen()
    print 'TODAVIA NO IMPLEMENTADO'
    raw_input('Intro para regresar ')

def gestionateAdd():
    refreshScreen()
    print 'TODAVIA NO IMPLEMENTADO'
    raw_input('Intro para regresar ')

def gestionateInfo():
    refreshScreen()
    c = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
    databases=c.database_names
    d = dict((db, [collection for collection in c[db].collection_names()])
             for db in c.database_names())
    for index,key in enumerate(d):
        print 'Base de datos',index,':',key
        print 'Lista de colecciones de',key
        for eachCollection in d[key]:
            print eachCollection
        print '\n\n'
    raw_input('Intro para regresar ')

def gestionateQuit():
    return 0

def gestionateMore():
    more=True
def gestionateDropBD():
    refreshScreen()
    client = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
    dbname=raw_input('Introduce el nombre de la base de datos que quieres borrar: ')
    if not dbname in client.database_names():
        print "La base de datos seleccionada no existe, usa el comando 'info' para ver las bases de datos disponibles"
    client.drop_database(dbname[:-1])
    raw_input('Completado, pulsa intro para regresar ')

def gestionateDropCOL():
    refreshScreen()
    client = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
    dbname=raw_input('Introduce el nombre de la base de la de datos de la que quieres borrar una coleccion: ')
    colname=raw_input('Introduce el nombre de la coleccion que quieres borrar: ')

    if not dbname in client.database_names():
        print "La coleccion seleccionada no existe, usa el comando 'info' para ver las bases de datos disponibles"
    if not colname in client[dbname].collection_names():
        print "La coleccion seleccionada no existe, usa el comando 'info' para ver las bases de datos disponibles"
    raw_input('Completado, pulsa intro para regresar ')
    client[dbname].drop_collection(colname)


def error():
    print 'La opcion introducida es incorrecta'
    time.sleep(0.5)
    

def gestionateInteraction(option):
    #This dictionary uses a switch for choose the option to execute
    optionsDict={
        'addDB': gestionateAddDB,
        'add': gestionateAdd,
        'info':gestionateInfo,
        'quit': gestionateQuit,
        'more':gestionateMore,
        'dropbd' : gestionateDropBD,
        'dropcol' : gestionateDropCOL
    }
    #Need to default a default function that will manage an incorrect output
    return optionsDict.get(option.lower(),error)()

def main():
    more=False
    printLogo()
   
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
    serverStatus=MakeDatabase.createDatabase(DropDatabase,DatabaseName)
    if not serverStatus:
        return -1

    print "FASE 2: Extraccion de las fases: "   
    allSections,allData=ExtractDataNames.main()
    MakeInsertionsToDatabaseNames.insertSections(allSections,DatabaseName)
    client = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
    mydb = client[configFile.DATABASE_NAME]
    mycol = mydb[configFile.COLLECTIONS_NAMES[0]]
    print "FASE 3: Extraccion de los datos: "
    allData,allClasses=ExtractDataData.main()
    print "FASE 4: Insercion de los datos: "
    MakeInsertionsToDatabaseData.insertData(allData,allClasses,DatabaseName)


    #Delete of the element that mantains open the connection

    mycol.delete_one({'TEST': 'TEST'})

    print 'EJECUCION COMPLETA SIN ERRORES :)'
    refreshScreen()
    option=''
    while option !='quit':
        option=raw_input('\n')
        gestionateInteraction(option) 
        refreshScreen()
    print 'SESION CERRADA'



if __name__=="__main__":
    main()
