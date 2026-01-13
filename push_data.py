import os
import sys
from pymongo import MongoClient
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

from dotenv import load_dotenv
load_dotenv()

try:
    MONGODB_URL = os.getenv('MONGODB_URL')
except Exception as e:
    raise CustomException(e)

class PushData:
    def __init__(self):
        pass

    def extract_data(self,file_path):
        try:
            data_df = pd.read_csv(file_path)
            data_df.reset_index(drop=True, inplace=True)

            logging.info("Data Extracted Sucessfully")
            return data_df
        except Exception as e:
            raise CustomException(e)
    
    def transform_data(self, data_df):
        try:
            transformed_data = data_df.to_dict(orient="records")

            logging.info("Data Transformed Sucessfully")
            return transformed_data
        
        except Exception as e:
            raise CustomException(e)
    
    def load_data(self,transformed_data):
        
        try:
            Database = 'phishingdb'
            Collection = 'phishing_collection'

            client = MongoClient(MONGODB_URL)
            db = client[Database]
            collection = db[Collection]

            collection.insert_many(transformed_data)

            logging.info("Data Loaded Sucessfully")

        except Exception as e:
            raise CustomException(e)



# pusher = PushData()
# Extracted_data = pusher.extract_data('raw_data/phisingData.csv')
# Transformed_data = pusher.transform_data(Extracted_data)
# pusher.load_data(Transformed_data)

