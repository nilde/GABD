#SERVER CONFIGURATION
SERVER_NAME="localhost"
PORT=27017

#CREATION SERVER OPTIONS
DATABASE_NAME="VECTORES_UCI"
COLLECTIONS_NAMES=['PRUEBA_1','PRUEBA_2','VECTORS']
COLLECTIONS_OPEN=[{"TEST": "TEST" },{ "TEST": "NIL"}]

#DATA_LOCATION_CONFIGURATION
VECTOR_PATH="../UCI/"
VECTOR_FILENAMES_DATA=['breast-cancer-wisconsin.data.txt','ionosphere.data.txt','iris.data.txt',
                        'letter-recognition.txt']
                        
VECTOR_FILENAMES_NAMES=['breast-cancer-wisconsin.names.txt','ionosphere.names.txt','letter-recognition.names']


#DATA_INSERTION_CONFIGURATION
INSERT_DATA=True
INSERT_NAMES=True
NUM_TUPLES_TO_INSERT=10
VERBOSE=False

