#!/usr/bin/python

#Contains all imports needed to resolve the dependencies
import sys
import configFile 
import pymongo
import platform
import time
import os

class ClientConsole(object):
    def __init__(self):
        self.client=object()
        self.option=''
        self.optionsDict={
            'addcol': self.gestionateAddCol,
            'info':self.gestionateInfo,
            'quit': self.gestionateQuit,
            'dropdb' : self.gestionateDropBD,
            'dropcol' : self.gestionateDropCOL,
            'usersinfo':self.manageUserProfiles
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
        print 'Introduce "addcol" para introducir un nuevo elemento en alguna coleccion'
        print 'Introduce "info" para obtener la informacion de la BD'
        print 'Introduce "more" para obtener la lista completa de comandos'
        print 'Introduce "dropdb" para eliminar una base de datos'
        print 'Introduce "dropcol" para eliminar una coleccion'
        print 'Introduce "usersInfo" para ver los diferentes perfiles asignados'
        print '----------------------------------------------------------\nCONSOLA:\n'


    

    def refreshScreen(self):

        if platform.system=='Windows':
            os.system('cls')
        else:
            os.system('clear')

        self.printLogo()
        self.printOptions()

    def gestionateAddCol(self):
        self.refreshScreen()

        db=raw_input('Introduce el nombre de la base de datos donde quieras crear la coleccion: ')
        col=raw_input('Introduce el nombre de la nueva coleccion: ')
        mydb=self.client[db]
        mycol=mydb[col]
        enteredOption='moi'

        mycolFieldsValues={}
        mycolFieldsContent={}

        acceptedTypes=['ObjectId','double','string','object','array',
                        'binData','undefined','bool','date','null','regex',
                        'dbPointer','javascript','symbol','javascriptWithScope',
                        'int','timestamp','long','decimal','minType','maxType']
        acceptedTypesExample =[
            '11111',0,'','null',[],0,'undefined',0,'ISODate("2014-01-01T08:15:39.736Z")','null',
            '*','','','','',0,'Timestamp(1412180887, 1)',0,0,-1,127 
        ]

        print 'Tipos de datos aceptados: ',', '.join(acceptedTypes)
        while enteredOption != '':
            enteredOption=raw_input('Introduce el nombre de un campo: ')
            typeOption=raw_input('Introduce un nuevo tipo: ')
            if typeOption in acceptedTypes or not enteredOption:
                mycolFieldsValues[enteredOption]=typeOption
            else:
                print 'Error en el tipo de datos vuelve a intentarlo'
        del mycolFieldsValues['']
        mydict={}
        
        for i in mycolFieldsValues:
            mydict[i]=acceptedTypesExample[acceptedTypes.index(mycolFieldsValues[i])]
        x = mycol.insert_one(mydict)
        raw_input('Completado,intro para regresar ')
    
    def manageUserProfiles(self):
        self.refreshScreen()
        content= self.client.VECT.command('usersInfo')
        for key in content['users']:
            print "DB: " + str(key["db"]) + " USER:"+ str(key["user"]) +" ROLES: " +str(key["roles"][-1]["role"])+ '\n'
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

    def testUser(self):
        print "No implementado aun"

    def gestionateDropBD(self):
        self.refreshScreen()
        dbname=raw_input('Introduce el nombre de la base de datos que quieres borrar: ')
        if not dbname in self.client.database_names():
            print "La base de datos seleccionada no existe, usa el comando 'info' para ver las bases de datos disponibles"
        self.client.drop_database(dbname)
        raw_input('Completado, pulsa intro para regresar ')

    def gestionateDropCOL(self):
        self.refreshScreen()
        dbname=raw_input('Introduce el nombre de la base de la de datos de la que quieres borrar una coleccion: ')
        colname=raw_input('Introduce el nombre de la coleccion que quieres borrar: ')

        if not dbname in self.client.database_names():
            print "La base de datos seleccionada no existe, usa el comando 'info' para ver las bases de datos disponibles"
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

    def start(self,client):
        self.client=client
        self.refreshScreen()    
        while self.option.lower() !='quit':
            self.option=raw_input('\n')
            self.gestionateInteraction() 
            self.refreshScreen()
        print 'SESION CERRADA'
