from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig, TrainingConfig

if __name__ == "__main__":
    training_config = TrainingConfig()
    data_ingestion_config = DataIngestionConfig(training_config)
    ingestion = DataIngestion(data_ingestion_config)
    ingestion.initiate_data_ingestion()
