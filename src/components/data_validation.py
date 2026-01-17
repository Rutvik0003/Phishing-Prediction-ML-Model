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
    def __init__(self, data_validation_config : DataValidationConfig, data_ingestion_artifact : DataIngestionArtifact, data_ingestion_config : DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_validation_config = data_validation_config

    def get_train_test_data(self):
        try:
            train_data_path = self.data_ingestion_artifact.train_data_path
            test_data_path = self.data_ingestion_artifact.test_data_path

            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)

            logging.info("Data Extracted Sucessfully - Data Validation")

            return train_data, test_data
        except Exception as e:
            raise CustomException(e,sys)
    
    def validate_columns(self, data : pd.DataFrame):
        try:
            schema_path = self.data_ingestion_config.training_config.schema_path
            schema_dict = read_yaml(schema_path)
            num_columns = schema_dict['dataset_schema']['total_columns']

            logging.info("Columns Validated Sucessfully")

            if(num_columns == len(data.columns)):
                return True
            return False
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def validate_data_drift(self, base_data : pd.DataFrame, current_data: pd.DataFrame, threshold : float):
        try:
            is_drift_found = False
            drift_report = {}

            for column in base_data.columns:
                d1 = base_data[column]
                d2 = current_data[column]

                drift = ks_2samp(d1, d2)

                column_drift = drift.pvalue < threshold

                drift_report[column] = {
                    "p_value": float(drift.pvalue),
                    "drift_detected": column_drift
                }

                if column_drift:
                    is_drift_found = True


                drift_report.update({
                    column: {
                    'drift': drift.pvalue,
                    'is_drift_found': is_drift_found
                    }
                })

                os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                report_path = self.data_validation_config.data_validation_report_path

                write_yaml(report_path, drift_report)

                logging.info("Drift Validated Sucessfully")

                return is_drift_found
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_validation(self):
        try:

            logging.info("Data Validation Initiated")
            train_data,test_data = self.get_train_test_data()
            train_data_validation = self.validate_columns(train_data)
            test_data_validation = self.validate_columns(test_data)
            is_drift_found = self.validate_data_drift(train_data,test_data,0.05)

            if(train_data_validation == True):
                valid_train_data_path = self.data_validation_config.valid_train_data_path
                invalid_train_data_path = None
                valid_dir_path = self.data_validation_config.valid_data_dir
                os.makedirs(valid_dir_path,exist_ok=True)
                train_data.to_csv(valid_train_data_path)

            else:
                valid_train_data_path = None
                invalid_train_data_path = self.data_validation_config.invalid_train_data_path
                invalid_dir_path = self.data_validation_config.invalid_data_dir
                os.makedirs(invalid_dir_path,exist_ok=True)
                train_data.to_csv(invalid_train_data_path)

            if(test_data_validation == True):
                valid_test_data_path = self.data_validation_config.valid_test_data_path
                invalid_test_data_path = None
                valid_dir_path = self.data_validation_config.valid_data_dir
                os.makedirs(valid_dir_path,exist_ok=True)
                test_data.to_csv(valid_test_data_path)
            else:
                valid_test_data_path = None
                invalid_test_data_path = self.data_ingestion_artifact.test_data_path
                invalid_dir_path = self.data_validation_config.invalid_test_data_path
                os.makedirs(invalid_dir_path,exist_ok=True)
                test_data.to_csv(invalid_test_data_path)

            data_validation_artifact = DataValidationArtifact(
                is_drift_found  = is_drift_found,
                train_data_validation_status = train_data_validation,
                test_data_validation_status = test_data_validation,
                valid_train_data_path = valid_train_data_path,
                invalid_train_data_path = invalid_train_data_path,
                valid_test_data_path = valid_test_data_path,
                invalid_test_data_path = invalid_test_data_path
            )

            print(data_validation_artifact)
            logging.info("Data Validation Completed")
            return data_validation_artifact
        except Exception as e:
            raise CustomException(e,sys)
        
        
            



    
        


