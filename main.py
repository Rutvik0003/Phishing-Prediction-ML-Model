from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

if __name__ == "__main__":
    data_ingestion_config = DataIngestionConfig()
    ingestion = DataIngestion(data_ingestion_config)
    ingestion.initiate_data_ingestion()
