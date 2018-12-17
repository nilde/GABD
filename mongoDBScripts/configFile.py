#SERVER CONFIGURATION
SERVER_NAME="localhost"
PORT=27017

#SERVER CREATION OPTIONS
DATABASE_NAME="VECTORES_UCI"
COLLECTIONS_NAMES=['DATABASES_INFO','RESULTS','SET_UP_EXPERIMENTS','METHODS','EXPERIMENTS','IMAGES']
COLLECTIONS_OPEN=[{"TEST": "TEST" },{"TEST": "TEST" },{"TEST": "TEST" },{"TEST": "TEST" },{"TEST": "TEST" },{"TEST": "TEST" }]

#DATA_LOCATION_CONFIGURATION
VECTOR_PATH="../UCI/"
VECTOR_FILENAMES_DATA=['breast-cancer-wisconsin.data.txt','ionosphere.data.txt','iris.data.txt',
                        'letter-recognition.txt']
VECTOR_FILENAMES_SECTIONS=['title','past_uses','source_information','number_of_instances','relevant_information','attribute_information','number_of_attributes','class_distribution','missing_values']
                        
VECTOR_FILENAMES_NAMES=['breast-cancer-wisconsin.names.txt','ionosphere.names.txt','iris.names.txt','letter-recognition.names']
VECTOR_FILENAMES_SHORT=['breast-cancer-wisconsin','ionosphere','iris',
                        'letter-recognition']

#METHODS_DATA_CONFIGURATION
METHOD_PATH="../METHODS_DATA/"
METHOD_FILENAME_NAMES="methods.name.txt"
METHOD_FILENAME_DATA="methods.txt"
METHOD_DATABASE="METHODS"


#RESULTS_DATA_CONFIGURATION
RESULT_PATH="../RESULTS_DATA/"
RESULT_FILENAME_NAMES="results.name.txt"
RESULT_FILENAME_DATA="results.txt"
RESULT_DATABASE="RESULTS"


#EXPERIMENTS_DATA_CONFIGURATION
EXPERIMENTS_PATH="../EXPERIMENTS_DATA/"
EXPERIMENTS_FILENAME_NAMES="experiments.name.txt"
EXPERIMENTS_FILENAME_DATA="experiments.txt"
EXPERIMENTS_DATABASE="EXPERIMENTS"


#IMAGES_DATA_INFORMATION
IMAGES_PATH="../IMAGES_PATH/"
IMAGES_CLASSES_FOLDER="CLASSES/"
IMAGES_CONTENT_FOLDER="IMAGES/"
IMAGES_V_CHARACTERISTICS_FOLDER="VECTORS/"
IMAGES_V_FILENAME_NAMES="neural_net.names.txt"
IMAGES_V_FILENAME_DATA="neural_nets.txt"
IMAGES_V_FILENAMES=['AlexNet1_4000','ResNet1_4000','VGG1_4000']
IMAGES_V_TYPES=['.Labelfeatures','.Sigmoidfeatures','.Visualfeatures']
IMAGE_DATABASE="NETS_IMAGES"

IMAGES_NUM_LINES=300


#DATA_INSERTION_CONFIGURATION
INSERT_DATA=True
INSERT_NAMES=True
#NUM_TUPLES_TO_INSERT=10
VERBOSE=False

