#!/usr/bin/python

#Contains all data needed to do the task
import configFile

#Library for use regex
import re

import string
class ExtractFromFile:
    def __init__(self):

        #Contain the methods definition column values
        self.allDataDescription=[]

        #Contain the all different methods information
        self.allDataValues=[]

    def getAllDataInformation(self):
        return self.allDataDescription,self.allDataValues

    def getAllDataDescriptions(self):
        return self.allDataDescription
    
    def getAllDataValues(self):
        return self.allDataValues

    def extractAllDataInformation(self,path,filename_names,filename_data):
        with open(path+filename_names) as f:
            self.allDataDescription = f.readlines()
            self.allDataDescription=[x.translate(string.maketrans("", "", ), '\n\r') for x in self.allDataDescription ]
        with open(path+filename_data) as f:
            self.allDataValues = f.readlines()
            self.allDataValues=[x.translate(string.maketrans("", "", ), '\n\r') for x in self.allDataValues ]

        self.allDataDescription=[i.split(',') for i in self.allDataDescription ][0]
        self.allDataValues= [i.split(',') for i in self.allDataValues]

    def makeExtraction(self,path,filename_names,filename_data):
        print " Extraccion de los metodos en proceso"
        self.extractAllDataInformation(path,filename_names,filename_data)
        return self.getAllDataInformation()
        print ' Extraccion de los metodos completada'
        print '//////////////////////////////////////////////////////////\n'
