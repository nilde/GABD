#!/usr/bin/python

#Contains all data needed to do the task
import configFile
import string

class extractData:
    def __init__(self):
        self.content=[]
        self.allClasses=[]
        self.allDataInformation=[]

    def openFileNames(self,path,filename):
        with open(path+filename) as f:
            self.content = f.readlines()

    def getContent(self):
        return self.content

    def getAllClasses(self):
        return self.allClasses

    def getAllDataInformation(self):
        return self.allDataInformation
        
    def extractAllDataInformation(self):
        for eachFilename in configFile.VECTOR_FILENAMES_DATA:
            with open(configFile.VECTOR_PATH+eachFilename) as f:
                self.content = f.readlines()
            self.content=[x.translate(string.maketrans("", "", ), '\n\r') for x in self.content ]
            self.allDataInformation.append(self.content)
            self.allClasses.append(eachFilename.split('.')[0])

    def makeExtraction(self):
        print " Extraccion de datos en proceso"
        self.extractAllDataInformation()
        print ' Extraccion de datos completada'
        print '//////////////////////////////////////////////////////////\n'
        return self.allClasses,self.allDataInformation
