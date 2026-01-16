from src.constants import training_pipeline_constants
import os


class TrainingConfig:
    def __init__(self):
        self.pipeline_name = training_pipeline_constants.PIPELINE_NAME
        self.artifact_dir_path = training_pipeline_constants.ARTIFACT_PATH


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
        
