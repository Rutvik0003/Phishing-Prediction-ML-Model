import os
import sys
import pandas as pd
import pymongo
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import CustomException
from src.logger import logging

import certifi
ca = certifi.where()

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def get_data_from_db(self):
        try:
            logging.info("Connecting to MongoDB")

            client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
            database = self.data_ingestion_config.database_name
            collection = self.data_ingestion_config.collection_name

            records = list(client[database][collection].find())
            df = pd.DataFrame(records)

            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)

            logging.info(f"Fetched {df.shape[0]} records from MongoDB")

            return df

        except Exception as e:
            raise CustomException(e,sys)

    def save_raw_data(self, data: pd.DataFrame):
        try:
            raw_path = self.data_ingestion_config.raw_data_path
            artifact_path = self.data_ingestion_config.artifact_path
            os.makedirs(artifact_path, exist_ok=True)
            os.makedirs(os.path.dirname(raw_path), exist_ok=True)

            data.to_csv(raw_path, index=False)
            logging.info(f"Raw data saved at {raw_path}")

        except Exception as e:
            raise CustomException(e,sys)

    def split_data(self, data: pd.DataFrame):
        try:
            train_ratio = self.data_ingestion_config.train_test_split_ratio

            train_data, test_data = train_test_split(
                data, test_size=train_ratio, random_state=42
            )

            logging.info("Train test split completed")

            return train_data, test_data

        except Exception as e:
            raise CustomException(e,sys)

    def save_train_test_split_data(self, train_data, test_data):
        try:
            train_path = self.data_ingestion_config.train_data_path
            test_path = self.data_ingestion_config.test_data_path

            os.makedirs(os.path.dirname(train_path), exist_ok=True)

            train_data.to_csv(train_path, index=False)
            test_data.to_csv(test_path, index=False)

            logging.info("Train and test data saved")

        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self):
        try:
            df = self.get_data_from_db()
            self.save_raw_data(df)
            train, test = self.split_data(df)
            self.save_train_test_split_data(train, test)
            data_ingestion_artifact = DataIngestionArtifact()
            data_ingestion_artifact.train_data_path = self.data_ingestion_config.train_data_path
            data_ingestion_artifact.test_data_path = self.data_ingestion_config.test_data_path

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e,sys)
