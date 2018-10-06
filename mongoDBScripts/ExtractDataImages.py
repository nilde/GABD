import glob
import configFile


#Extracts and put in a list all the tags relateed with images
dataToInsert=[]
cleanedNames=[]
listWithAllClasses=glob.glob(configFile.IMAGES_PATH+configFile.IMAGES_CLASSES_FOLDER+"*.txt")
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


