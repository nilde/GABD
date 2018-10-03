#SERVER CONFIGURATION
SERVER_NAME="localhost"
PORT=27017

#SERVER CREATION OPTIONS
DATABASE_NAME="VECTORES_UCI"
COLLECTIONS_NAMES=['DATABASES_INFO','RESULTS','SET_UP_EXPERIMENTS','METHODS','EXPERIMENTS','VECTORS']
COLLECTIONS_OPEN=[{"TEST": "TEST" },{"TEST": "TEST" },{"TEST": "TEST" },{"TEST": "TEST" },{"TEST": "TEST" },{"TEST": "TEST" }]

#DATA_LOCATION_CONFIGURATION
VECTOR_PATH="../UCI/"
VECTOR_FILENAMES_DATA=['breast-cancer-wisconsin.data.txt','ionosphere.data.txt','iris.data.txt',
                        'letter-recognition.txt']
VECTOR_FILENAMES_SECTIONS=['title','past_uses','source_information','number_of_instances','relevant_information','attribute_information','number_of_attributes','class_distribution','missing_values']
                        
VECTOR_FILENAMES_NAMES=['breast-cancer-wisconsin.names.txt','ionosphere.names.txt','letter-recognition.names']
VECTOR_FILENAMES_SHORT=['breast-cancer-wisconsin','ionosphere','iris',
                        'letter-recognition']



METHOD_PATH="../METHODS_DATA/"
METHOD_FILENAME_NAMES="methods.name.txt"
METHOD_FILENAME_DATA="methods.txt"
METHOD_DATABASE="METHODS"

RESULT_PATH="../RESULTS_DATA/"
RESULT_FILENAME_NAMES="results.name.txt"
RESULT_FILENAME_DATA="results.txt"
RESULT_DATABASE="RESULTS"

#DATA_INSERTION_CONFIGURATION
INSERT_DATA=True
INSERT_NAMES=True
#NUM_TUPLES_TO_INSERT=10
VERBOSE=False

