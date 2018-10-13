import glob
import configFile
import struct
import numpy as np


#Extracts and put in a list all the tags relateed with images
dataToInsert=[]
cleanedNames=[]
listWithAllClasses=glob.glob(configFile.IMAGES_PATH+configFile.IMAGES_CLASSES_FOLDER+"*.txt")

########
#EXTRACT ALL CLASSES INFORMATION
for eachClass in listWithAllClasses:
    cleanedName=eachClass.split('/')[-1].split('.')[0]
    cleanedNames.append(cleanedName)
    dataToInsert.append({cleanedName:[]})

for i,eachClassPath in enumerate(listWithAllClasses):
        with open(eachClassPath) as f:
            allContentReaded=f.readlines()
        for eachLine in allContentReaded:
            dataToInsert[i][cleanedNames[i]].append(eachLine[:-2])
        allContentReaded=[]


#print dataToInsert


#FINISH OF EXTRACTION OF ALL CLASSES INFORMATION

#EXTRACT NUMBER OF LINES OF A VECTOR IMAGE FILE NOT ALL WILL BE HARD TO DEBUG


bigBuffer=[]
for eachFileNet in configFile.IMAGES_V_FILENAMES:
    data=[]
    for eachFileType in configFile.IMAGES_V_TYPES:
        dimension=[]

        with open(configFile.IMAGES_PATH+configFile.IMAGES_V_CHARACTERISTICS_FOLDER+eachFileNet+eachFileType) as myfile:
          dimension = [next(myfile,'') for x in xrange(25000)]

        dimension=dimension[0][:-1]
        dimension=dimension.split(' ')

        # load feature vector
        shape = (int(dimension[0]), int(dimension[1]))
        with open(configFile.IMAGES_PATH+configFile.IMAGES_V_CHARACTERISTICS_FOLDER+eachFileNet+eachFileType,'rb') as fid:
            #REVISAR EL FORMATO DE LOS DATOS
            data = np.fromfile(fid, count=np.prod(shape),dtype = np.uint16)
        data.shape = shape
        bigBuffer.append(data)



#Los datos se guardan como se debe en un matriz de dimensiones 3x2500xN aun falta convertirla en una matriz que 
finalData=[]
print len(bigBuffer)
for index in range(0,9,3):
    netContent=[]
    for length in range(len(bigBuffer[index][:])):
        netContent.append([bigBuffer[index][length][:],bigBuffer[index+1][length][:],bigBuffer[index+2][length][:]])
    finalData.append(netContent)



#Para ordenar lo que se recibe del pymongo
 #as_class=OrderedDict
