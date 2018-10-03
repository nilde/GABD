#!/usr/bin/python

#Contains all data needed to do the task
import configFile

#Library for use regex
import re

import string
class ExtractResults:
    def __init__(self):
        self.content=[]

        #Contain the methods definition column values
        self.allResultsDescriptions=[]

        #Contain the all different methods information
        self.allResultsValues=[]

    def getAllResultsInformation(self):
        return self.allResultsDescriptions,self.allResultsValues
    def getAllResultsDescriptions(self):
        return self.allResultsDescriptions
    
    def getAllResultsValues(self):
        return self.allResultsValues

    def extractAllResultsInformation(self):
        with open(configFile.RESULT_PATH+configFile.RESULT_FILENAME_NAMES) as f:
            self.allResultsDescriptions = f.readlines()
            self.allResultsDescriptions=[x.translate(string.maketrans("", "", ), '\n\r') for x in self.allResultsDescriptions ]
        with open(configFile.RESULT_PATH+configFile.RESULT_FILENAME_DATA) as f:
            self.allResultsValues = f.readlines()
            self.allResultsValues=[x.translate(string.maketrans("", "", ), '\n\r') for x in self.allResultsValues ]

        self.allResultsDescriptions=[i.split(',') for i in self.allResultsDescriptions ][0]
        self.allResultsValues= [i.split(',') for i in self.allResultsValues]

    def makeExtraction(self):
        print " Extraccion de los metodos en proceso"
        self.extractAllResultsInformation()
        return self.getAllResultsInformation()
        print ' Extraccion de los metodos completada'
        print '//////////////////////////////////////////////////////////\n'
