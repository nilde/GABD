#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import pymongo

class InsertionUsers:
    def __init__(self,client):
        client.VECT.add_user('detector_outliers', 'detector_outliers', roles=[{'role':'read','db':'VECT'}]) #correcto
        client.VECT.add_user('gestor_dades', 'gestor_dades', roles=[{'role':'readWrite','db':'VECT'}]) #correcto
        client.VECT.add_user('desenvolupador', 'desenvolupador', roles=[{'role':'dbAdmin','db':'VECT'}]) #correcto
        client.VECT.add_user('auditors', 'auditors', roles=[{'role':'read','db':'VECT'}]) #correcto
        #use VECT
        #db.grantRolesToUser("auditors", ["hostManager"])
        # db.updateUser("auditor",{ roles: [{role: "hostManager",db:"VECT"}]} )
        print client.VECT.command('usersInfo')
        raw_input('c')
        


            
        

