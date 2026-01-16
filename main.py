from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.entity.config_entity import DataIngestionConfig, TrainingConfig, DataValidationConfig

if __name__ == "__main__":
    training_config = TrainingConfig()
    data_ingestion_config = DataIngestionConfig(training_config)
    ingestion = DataIngestion(data_ingestion_config)
    data_ingestion_artifact = ingestion.initiate_data_ingestion()
    data_validation_config = DataValidationConfig(data_ingestion_config)
    validation = DataValidation(data_validation_config,data_ingestion_artifact,data_ingestion_config)
    data_validation_artifact = validation.initiate_data_validation()
    
    
