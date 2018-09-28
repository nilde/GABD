import pymongo
import configFile


#Simple function that creates a new DB,remember that you need to introduce 
# at least one element to mantain created the collection.
def createDatabase(DropDatabase,DatabaseName):
    print ' Creacion de la base de datos en proceso'
    client = pymongo.MongoClient(configFile.SERVER_NAME,configFile.PORT)
    if DropDatabase:
        client.drop_database(DatabaseName)
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("Server not available")
        return 0
    mydb = client[DatabaseName]

    #Create new collection for each database collection needed.
    for indexCollection,eachCollection in enumerate(configFile.COLLECTIONS_NAMES[:-1]):
        mycol = mydb[configFile.COLLECTIONS_NAMES[indexCollection]]
        mydict = configFile.COLLECTIONS_OPEN[indexCollection]
        x = mycol.insert_one(mydict)
    print ' Creacion de la base de datos realizada'
    print '//////////////////////////////////////////////////////////\n'

    return 1
