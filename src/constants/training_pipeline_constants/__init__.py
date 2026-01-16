import os

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

DATA_VALIDATION_DIR = 'data_validation'
DATA_VALIDATION_VALID_DIR = 'valid'
DATA_VALIDATION_INVALID_DIR = 'invalid'
DATA_VALIDATION_VALID_TRAIN_DATA = 'valid_train_data'
DATA_VALIDATION_VALID_TEST_DATA = 'valid_test_data'
DATA_VALIDATION_INVALID_TRAIN_DATA = 'invalid_train_data'
DATA_VALIDATION_INVALID_TEST_DATA = 'invalid_test_data'



