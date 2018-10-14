import glob
import configFile
import struct
import numpy as np
from ExtractDataResults import ExtractFromFile

class ExtractFromImagesFiles:
    def __init__(self):
        self.classesInformation=[]
        self.rawVectorsInformation=[]
        self.vectorsInformationCorretly=[]
        self.DataExtractorForNetsInfo=ExtractFromFile()
        self.allNetsInformation,self.allNetsData=self.DataExtractorForNetsInfo.makeExtraction(configFile.IMAGES_PATH,configFile.IMAGES_V_FILENAME_NAMES,configFile.IMAGES_V_FILENAME_DATA)
    
    def extractNetsInformation(self): 
        cleanedNames=[]
        listWithAllClasses=glob.glob(configFile.IMAGES_PATH+configFile.IMAGES_CLASSES_FOLDER+"*.txt")

        #EXTRACT ALL CLASSES INFORMATION
        for eachClass in listWithAllClasses:
            cleanedName=eachClass.split('/')[-1].split('.')[0]
            cleanedNames.append(cleanedName)
            self.classesInformation.append({cleanedName:[]})

        for i,eachClassPath in enumerate(listWithAllClasses):
            with open(eachClassPath) as f:
                allContentReaded=f.readlines()
            for eachLine in allContentReaded:
                self.classesInformation[i][cleanedNames[i]].append(eachLine[:-2])
            allContentReaded=[]

    def extractRawVectorsInformation(self):
            
        for eachFileNet in configFile.IMAGES_V_FILENAMES:
            data=[]
            for eachFileType in configFile.IMAGES_V_TYPES:
                dimension=[]

                with open(configFile.IMAGES_PATH+configFile.IMAGES_V_CHARACTERISTICS_FOLDER+eachFileNet+eachFileType) as myfile:
                    dimension = [next(myfile,'') for x in xrange(1)]

                dimension=dimension[0][:-1]
                dimension=dimension.split(' ')

                # load feature vector
                shape = (int(dimension[0]), int(dimension[1]))
                with open(configFile.IMAGES_PATH+configFile.IMAGES_V_CHARACTERISTICS_FOLDER+eachFileNet+eachFileType,'rb') as fid:
                    #REVISAR EL FORMATO DE LOS DATOS
                    data = np.fromfile(fid, count=np.prod(shape),dtype = np.uint16)
                data.shape = shape
                self.rawVectorsInformation.append(data)
        


    def makeDataCorretly(self):
        #Los datos se guardan como se debe en un matriz de dimensiones 3x2500xN aun falta convertirla en una matriz que 
        finalData=[]

        for index in range(0,9,3):
            netContent=[]
            for length in range(len(self.rawVectorsInformation[index][:])):
                netContent.append([self.rawVectorsInformation[index][length][:],self.rawVectorsInformation[index+1][length][:],self.rawVectorsInformation[index+2][length][:]])
            finalData.append(netContent)

        for eachNet in finalData:
            netsWithImageID={}
            for i,eachVectors in enumerate(eachNet):
                netsWithImageID[str(i)]=[x for x in eachVectors]
            self.vectorsInformationCorretly.append(netsWithImageID)
    def makeExtraction(self):
        self.extractNetsInformation()
        self.extractRawVectorsInformation()
        self.makeDataCorretly()

        return self.allNetsInformation,self.allNetsData,self.classesInformation,self.vectorsInformationCorretly
