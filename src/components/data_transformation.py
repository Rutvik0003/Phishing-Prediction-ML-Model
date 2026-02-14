import sys
import os
import numpy as np
import pandas as pd

from src.entity.artifact_entity import DataValidationArtifact
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataTransformationArtifact

from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer

from src.utils import save_numpy_obj, save_pickle_obj

from src.constants.training_pipeline_constants import DATA_IMPUTATION_PARAMETERS

from src.exception import CustomException
from src.logger import logging

class DataTransformation:
    def __init__(self, data_validation_artifact : DataValidationArtifact, data_transformation_config : DataTransformationConfig):
        self.data_transformation_config = data_transformation_config
        self.data_validation_artifcat = data_validation_artifact

    def get_train_test_data(self):
        try:
            logging.info("Started Retriving Data for Transformation")
            train_data_path = self.data_validation_artifcat.valid_train_data_path
            test_data_path = self.data_validation_artifcat.valid_test_data_path

            train_data_df = pd.read_csv(train_data_path)
            test_data_df = pd.read_csv(test_data_path)

            logging.info("Data Retrieved Sucessfully")

            return train_data_df, test_data_df
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_processing_object(self):

        try:

            logging.info("initialising imputer")
            imputer = KNNImputer(**DATA_IMPUTATION_PARAMETERS)
            processor = Pipeline([('imputer', imputer)])

            return processor
        
        except Exception as e:
            raise CustomException(e,sys)
    

    def create_data_transformation_artifact(self):
        try:
            logging.info("artifact creation started")    
            data_transformation_artifact = DataTransformationArtifact(
                train_data_arr_path = self.data_transformation_config.train_data_arr_path,
                test_data_arr_path = self.data_transformation_config.test_data_arr_path,
                preprocessing_obj_path = self.data_transformation_config.preprocessing_obj_path
            )
            

            logging.info('artifact created')
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e,sys)   
        
    def initialise_data_transformation(self):

        try:
            logging.info('Data Transformation Initiated')
            train_data, test_data = self.get_train_test_data()
                
            input_train_data_df = train_data.drop(columns = ['Result'], axis = 1)
            target_train_data_df = train_data['Result']
            target_train_data_df = target_train_data_df.replace(-1,0)

            input_test_data_df = test_data.drop(columns = ['Result'], axis = 1)
            target_test_data_df = test_data['Result']
            target_test_data_df = target_test_data_df.replace(-1,0)

            logging.info("Input and Target data saperated Sucessfully")

            processor_obj = self.get_processing_object()
            transformed_input_train_data_array = processor_obj.fit_transform(input_train_data_df) 
            transformed_input_test_data_array = processor_obj.transform(input_test_data_df)

            train_data_array = np.c_[transformed_input_train_data_array, target_train_data_df.values]
            test_data_array = np.c_[transformed_input_test_data_array, target_test_data_df.values]

            logging.info("Data Transformed Sucessfully")

            train_data_array_path = self.data_transformation_config.train_data_arr_path
            test_data_array_path = self.data_transformation_config.test_data_arr_path
            preprocessing_obj_path = self.data_transformation_config.preprocessing_obj_path

            save_numpy_obj(train_data_array, train_data_array_path)
            save_numpy_obj(test_data_array, test_data_array_path)
            save_pickle_obj(processor_obj, preprocessing_obj_path)

            logging.info("Data Saved Sucessfully")

            data_transformation_artifact = self.create_data_transformation_artifact()
            print(data_transformation_artifact)

            return data_transformation_artifact
        
        except Exception as e:
            raise CustomException(e,sys)
    
           

        

    


        

        
