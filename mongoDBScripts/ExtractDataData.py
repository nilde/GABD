#!/usr/bin/python

#Contains all data needed to do the task
import configFile

#Library for use regex
import re

import string

def openFileNames(path,filename):
    with open(path+filename) as f:
        content = f.readlines()

    return content

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


def extractAllDataInformation():
    allDataInformation=[]
    allClasses=[]
    for eachFilename in configFile.VECTOR_FILENAMES_DATA:
        with open(configFile.VECTOR_PATH+eachFilename) as f:
            content = f.readlines()
        content=[x.translate(string.maketrans("", "", ), '\n\r') for x in content ]
        allDataInformation.append(content)
        allClasses.append(eachFilename.split('.')[0])
    return allClasses,allDataInformation

def main():
    print " Extraccion de datos en proceso"
    allClasses,allData=extractAllDataInformation()

    print ' Extraccion de datos completada'
    print '//////////////////////////////////////////////////////////\n'
    return allData,allClasses

if __name__=="__main__":
    main()
