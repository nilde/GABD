#!/usr/bin/python

#Contains all data needed to do the task
import configFile

#Library for use regex
import re

import string
class ExtractMethods:
    def __init__(self):
        self.content=[]

        #Contain the methods definition column values
        self.allMethodsDescriptions=[]

        #Contain the all different methods information
        self.allMethodsValues=[]

    def getAllMethodsInformation(self):
        return self.allMethodsDescriptions,self.allMethodsValues
    def getAllMehodsDescriptions(self):
        return self.allMethodsDescriptions
    
    def getAllMehodsValues(self):
        return self.allMethodsValues

    def extractAllMethodInformation(self):
        with open(configFile.METHOD_PATH+configFile.METHOD_FILENAME_NAMES) as f:
            self.allMethodsDescriptions = f.readlines()
            self.allMethodsDescriptions=[x.translate(string.maketrans("", "", ), '\n\r') for x in self.allMethodsDescriptions ]
        with open(configFile.METHOD_PATH+configFile.METHOD_FILENAME_DATA) as f:
            self.allMethodsValues = f.readlines()
            self.allMethodsValues=[x.translate(string.maketrans("", "", ), '\n\r') for x in self.allMethodsValues ]

        self.allMethodsDescriptions=[i.split(',') for i in self.allMethodsDescriptions ][0]
        self.allMethodsValues= [i.split(',') for i in self.allMethodsValues]

    def makeExtraction(self):
        print " Extraccion de los metodos en proceso"
        self.extractAllMethodInformation()
        print ' Extraccion de los metodos completada'
        print '//////////////////////////////////////////////////////////\n'
