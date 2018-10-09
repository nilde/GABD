import glob
import configFile
import struct


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



for eachFile in configFile.IMAGES_V_FILENAMES:
    dimension=[]
    with open(configFile.IMAGES_PATH+configFile.IMAGES_V_CHARACTERISTICS_FOLDER+eachFile) as myfile:
        dimension = [next(myfile,'')for x in xrange(1)]

    dimension=dimension[0][:-1]
    dimension=dimension.split(' ')
    print dimension
    # load feature vector

    f = open(configFile.IMAGES_PATH+configFile.IMAGES_V_CHARACTERISTICS_FOLDER+eachFile, 'r')
    dims = [int(val) for val in f.readline().rstrip("\n").split(" ")]
    x = f.read()
    f.close()
    size = int(4)  # bytes to represent each float
    totalVectorContent=[]
    for i in range(0, dims[0]):
        bf = x[i * dims[1] * size:(i + 1) * size * dims[1]]
        numFeatures = len(bf) / size
        features = list(struct.unpack(dimension[1]+'f', bf))
        totalVectorContent.append( features)
    print totalVectorContent[0]


