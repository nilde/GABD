#!/usr/bin/python

#Contains all data needed to do the task
import configFile

#Library for use regex
import re

import string

def openFileNames(path,filename):
    with open(path+filename) as f:
        content = f.readlines()

    #Contain all content from file
    allContent=[x.translate(string.maketrans("", "", ), '\n') for x in content ]
    #Just contain the different titles from the file 
    contentSections=[x.strip('\n') for x in content if re.match('^[-+]?[0-9]+$',x[0])]
    return allContent,contentSections

def generateSeparatedContent(allContent,contentSections):
    initialIndex=0
    lastIndex=0
    allSeparatedSections=[]
    eachSectionContent=[]

    #Iteration over all content file knowing when a section is finish and saving it apart
    for eachSectionTitle in contentSections[1:]:
        lastIndex=allContent.index(eachSectionTitle)
        eachSectionContent=allContent[initialIndex:lastIndex]
        allSeparatedSections.append(eachSectionContent)
        eachSectionContent=[]
        initialIndex=lastIndex-1

    #Append the last section of the document
    allSeparatedSections.append(allContent[lastIndex:-1])
    return allSeparatedSections

#Put all separated lines readed from eachSection together
def putExtractedDataTogether(extractedData):
    extractedDataCleaned=[]
    temporalBuffer=[]
    for eachSection in extractedData:
        temporalBuffer.append(''.join(eachSection))
        extractedDataCleaned.append(temporalBuffer)
        temporalBuffer=[]
    return extractedDataCleaned

#This function work as root from the reading and pushing all content to the database (not yet)
def extractNamesData(path,filename):
    allContent,contentSections=openFileNames(path,filename)
    extractedData=generateSeparatedContent(allContent,contentSections)
    extractedDataCleaned=putExtractedDataTogether(extractedData)
    return extractedDataCleaned


def extractAllSectionsInformation():
    allSectionsInformation=[]
    for eachFilenameNames in configFile.VECTOR_FILENAMES_NAMES:
        extractedDataSections=extractNamesData(configFile.VECTOR_PATH,eachFilenameNames)
        allSectionsInformation.append(extractedDataSections)
        if configFile.VERBOSE==True:
            print extractedDataSections,'\n'

    return allSectionsInformation



def extractAllDataInformation():
    allDataInformation=[]
    for eachFilename in configFile.VECTOR_FILENAMES_DATA:
        with open(configFile.VECTOR_PATH+eachFilename) as f:
            content = f.readlines()
        content=[x.translate(string.maketrans("", "", ), '\n\r') for x in content ]
        allDataInformation.append(content)
    return allDataInformation

def main():
    print ' Extraccion de datos en proceso'
    allSections=extractAllSectionsInformation()
    allData=extractAllDataInformation()

    print ' Extraccion de datos completada'
    print '//////////////////////////////////////////////////////////\n'
    return allSections,allData

if __name__=="__main__":
    main()
