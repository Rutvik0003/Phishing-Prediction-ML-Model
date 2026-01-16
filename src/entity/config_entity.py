from src.constants import training_pipeline_constants
import os


class TrainingConfig:
    def __init__(self):
        self.pipeline_name = training_pipeline_constants.PIPELINE_NAME
        self.artifact_dir_path = training_pipeline_constants.ARTIFACT_PATH
        self.schema_path = training_pipeline_constants.SCHEMA_PATH


class DataIngestionConfig:
    def __init__(self, training_config:TrainingConfig):
        self.training_config = training_config

        self.database_name = training_pipeline_constants.DATABASE_NAME
        self.collection_name = training_pipeline_constants.COLLECTION_NAME
        self.ingestion_dir_path = os.path.join(training_config.artifact_dir_path,training_pipeline_constants.INGESTION_FOLDER)
        self.raw_data_path = os.path.join(self.ingestion_dir_path, training_pipeline_constants.RAW_DATA_PATH)
        self.train_test_split_ratio = training_pipeline_constants.TRAIN_TEST_SPLIT_RATIO
        self.train_data_path = os.path.join(self.ingestion_dir_path, training_pipeline_constants.TRAIN_DATA_PATH)
        self.test_data_path = os.path.join(self.ingestion_dir_path, training_pipeline_constants.TEST_DATA_PATH)
        

class DataValidationConfig:
    def __init__(self, data_ingestion_config : DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.data_validation_dir = os.path.join(data_ingestion_config.training_config.artifact_dir_path,training_pipeline_constants.DATA_VALIDATION_DIR)
        self.valid_data_dir = os.path.join(self.data_validation_dir, training_pipeline_constants.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir = os.path.join(self.data_validation_dir, training_pipeline_constants.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_data_path = os.path.join(self.valid_data_dir, training_pipeline_constants.DATA_VALIDATION_VALID_TRAIN_DATA)
        self.valid_test_data_path = os.path.join(self.valid_data_dir, training_pipeline_constants.DATA_VALIDATION_VALID_TEST_DATA)
        self.invalid_train_data_path = os.path.join(self.invalid_data_dir, training_pipeline_constants.DATA_VALIDATION_INVALID_TRAIN_DATA)
        self.invalid_test_data_path = os.path.join(self.invalid_data_dir, training_pipeline_constants.DATA_VALIDATION_INVALID_TEST_DATA)
        self.data_validation_report_path = os.path.join(self.data_validation_dir, training_pipeline_constants.DATA_VALIDATION_REPORT)


