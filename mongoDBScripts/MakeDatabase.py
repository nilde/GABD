import pymongo
import configFile


#Simple function that creates a new DB,remember that you need to introduce 
# at least one element to mantain created the collection.
def createDatabase(DropDatabase,DatabaseName):
    print ' Creacion de la base de datos en proceso'
    
    try:
        client = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT,
            serverSelectionTimeoutMS=1000)
        if DropDatabase:
            client.drop_database(DatabaseName)
        mydb = client[DatabaseName]
        #Create new collection for each database collection needed.
        for indexCollection,eachCollection in enumerate(configFile.COLLECTIONS_NAMES[:-1]):
            mycol = mydb[configFile.COLLECTIONS_NAMES[indexCollection]]
            mydict = configFile.COLLECTIONS_OPEN[indexCollection]
            x = mycol.insert_one(mydict)
        print ' Creacion de la base de datos realizada'
        print '//////////////////////////////////////////////////////////\n'
        return 1,client
    except Exception as e:
        print(" MONGODB NO ESTA ENCENDIDO")
        return 0,''
    

    
