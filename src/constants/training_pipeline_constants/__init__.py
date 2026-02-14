import os
import numpy as np

PIPELINE_NAME: str = "PhishingPredictionTrainingPipeline"
ARTIFACT_PATH: str = "artifacts"

SCHEMA_PATH = os.path.join('schema','data_schema.yaml')


#Ingestion Constants
INGESTION_FOLDER: str = "ingestion"
FEATURE_FOLDER: str = "feature"

RAW_DATA_PATH: str = "raw_data.csv"
TRAIN_DATA_PATH: str = "train.csv"
TEST_DATA_PATH: str = "test.csv"

TRAIN_TEST_SPLIT_RATIO: float = 0.3

DATABASE_NAME: str = "phishingdb"
COLLECTION_NAME: str = "phishing_collection"

#Validation Constants

DATA_VALIDATION_REPORT = 'report.yaml'
DATA_VALIDATION_DIR = 'data_validation'
DATA_VALIDATION_VALID_DIR = 'valid'
DATA_VALIDATION_INVALID_DIR = 'invalid'
DATA_VALIDATION_VALID_TRAIN_DATA = 'valid_train_data'
DATA_VALIDATION_VALID_TEST_DATA = 'valid_test_data'
DATA_VALIDATION_INVALID_TRAIN_DATA = 'invalid_train_data'
DATA_VALIDATION_INVALID_TEST_DATA = 'invalid_test_data'


##Data Transformation

DATA_TRANSFORMATION_DIR = 'data_transformation'
TRAIN_ARRAY_FILE_NAME = 'train_data_array.npy'
TEST_ARRAY_FILE_NAME = 'test_data_array.npy'
PROCESSOR_OBJ_FILE_NAME = 'preprocessor.pkl'

DATA_IMPUTATION_PARAMETERS : dict = {
    'missing_values': np.nan,
    'n_neighbors' : 5,
    'weights' : 'uniform'
}

##Model Trainer

MODEL_TRAINING_DIR = 'model_trainer'
TRAINED_MODEL_NAME = 'trained_model.pkl'



