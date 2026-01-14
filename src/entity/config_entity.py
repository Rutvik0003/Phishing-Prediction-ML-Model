from src.constants import training_pipeline_constants


class TrainingConfig:
    def __init__(self):
        pass


class DataIngestionConfig:
    def __init__(self, training_config=None):
        self.training_config = training_config or TrainingConfig()

        self.database_name = training_pipeline_constants.DATABASE_NAME
        self.collection_name = training_pipeline_constants.COLLECTION_NAME
        self.raw_data_path = training_pipeline_constants.RAW_DATA_PATH
        self.train_test_split_ratio = training_pipeline_constants.TRAIN_TEST_SPLIT_RATIO
        self.train_data_path = training_pipeline_constants.TRAIN_DATA_PATH
        self.test_data_path = training_pipeline_constants.TEST_DATA_PATH
        self.artifact_path = training_pipeline_constants.ARTIFACT_PATH
