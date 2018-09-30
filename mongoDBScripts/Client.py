#!/usr/bin/python

#Contains all imports needed to resolve the dependencies
import sys
import configFile 
import pymongo
import platform
import time

class ClientConsole(object):
    def __init__(self):
        self.client=pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
        self.option=''
        self.optionsDict={
            'adddb': self.gestionateAddDB,
            'addcol': self.gestionateAdd,
            'info':self.gestionateInfo,
            'quit': self.gestionateQuit,
            'dropdb' : self.gestionateDropBD,
            'dropcol' : self.gestionateDropCOL
        }

    def printLogo(self):
        print "\n"
        print "     xxxxxxxxxxxxxxxxxxxxxxx     " 
        print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        print "   ___     ___     ___     ___  " 
        print " /  __|   /   \   | _ )   |   \  "
        print " | (_ |   | - |   | _ \   | |) | "
        print "  \___|   |_|_|   |___/   |___/  "
        print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        print "     xxxxxxxxxxxxxxxxxxxxxxx     \n\n" 

    def printOptions(self):
        print 'Introduce "quit" para cerrar la sesion'
        print 'Introduce "adddb" para introducir una base de de datos'
        print 'Introduce "addcol" para introducir un nuevo elemento en alguna coleccion'
        print 'Introduce "info" para obtener la informacion de la BD'
        print 'Introduce "more" para obtener la lista completa de comandos'
        print 'Introduce "dropdb" para eliminar una base de datos'
        print 'Introduce "dropcol" para eliminar una coleccion'
        print 'y 0 mas (introduce "more" para ver todos los comandos)'
        print '----------------------------------------------------------\nCONSOLA:\n'

    def refreshScreen(self):

        if platform.system=='Windows':
            os.system('cls')
        else:
            os.system('clear')

        self.printLogo()
        self.printOptions()

    def gestionateAddDB(self):
        self.refreshScreen()
        print 'TODAVIA NO IMPLEMENTADO'
        raw_input('Intro para regresar ')

    def gestionateAdd(self):
        self.refreshScreen( )
        print 'TODAVIA NO IMPLEMENTADO'
        raw_input('Intro para regresar ')

    def gestionateInfo(self):
        self.refreshScreen()
        databaseInfo = dict((db, [collection for collection in self.client[db].collection_names()])
             for db in self.client.database_names())
        for index,key in enumerate(databaseInfo):
            print 'Base de datos',index,':',key
            print 'Lista de colecciones de',key
            for eachCollection in databaseInfo[key]:
                print eachCollection
            print '\n\n'
        raw_input('Intro para regresar ')

    def gestionateQuit(self):
        return 0

    def gestionateDropBD(self):
        self.refreshScreen()
        dbname=raw_input('Introduce el nombre de la base de datos que quieres borrar: ')
        print dbname
        print self.client.database_names()
        if not dbname in self.client.database_names():
            print "La base de datos seleccionada no existe, usa el comando 'info' para ver las bases de datos disponibles"
        self.client.drop_database(dbname)
        raw_input('Completado, pulsa intro para regresar ')

    def gestionateDropCOL(self):
        self.refreshScreen()
        dbname=raw_input('Introduce el nombre de la base de la de datos de la que quieres borrar una coleccion: ')
        colname=raw_input('Introduce el nombre de la coleccion que quieres borrar: ')

        if not dbname in self.client.database_names():
            print "La coleccion seleccionada no existe, usa el comando 'info' para ver las bases de datos disponibles"
        if not colname in self.client[dbname].collection_names():
            print "La coleccion seleccionada no existe, usa el comando 'info' para ver las bases de datos disponibles"
        raw_input('Completado, pulsa intro para regresar ')
        self.client[dbname].drop_collection(colname)


    def error(self):
        print 'La opcion introducida es incorrecta'
        time.sleep(0.5)
    

    def gestionateInteraction(self):
        #Need to default a default function that will manage an incorrect output
        return self.optionsDict.get(self.option.lower(),self.error)()

    def start(self):
        self.refreshScreen()    
        while self.option !='quit':
            self.option=raw_input('\n')
            self.gestionateInteraction() 
            self.refreshScreen()
        print 'SESION CERRADA'
