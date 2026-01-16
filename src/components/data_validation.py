import os
import sys

from src.exception import CustomException
from src.logger import logging

import numpy as np
import pandas as pd

from scipy.stats import ks_2samp

from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig
from src.utils import read_yaml,write_yaml



class DataValidation:
    def __init__(self, data_ingestion_artifact : DataIngestionArtifact, data_ingestion_config : DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.data_ingestion_artifact = data_ingestion_artifact

    def get_train_test_data(self):
        train_data_path = self.data_ingestion_artifact.train_data_path
        test_data_path = self.data_ingestion_artifact.test_data_path

        train_data = pd.read_csv(train_data_path)
        test_data = pd.read_csv(test_data_path)

        return train_data, test_data
    
    def validate_columns(self, data : pd.DataFrame):

        schema_path = self.data_ingestion_config.training_config.schema_path
        schema_dict = read_yaml(schema_path)
        num_columns = schema_dict['dataset_schema']['total_columns']

        if(num_columns == len(data.columns)):
            return True
        return False
    
    # def validate_data_drift(self, data : pd.DataFrame):

    
    
        


