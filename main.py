from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import DataIngestionConfig, TrainingConfig, DataValidationConfig, DataTransformationConfig

if __name__ == "__main__":
    training_config = TrainingConfig()
    data_ingestion_config = DataIngestionConfig(training_config)
    ingestion = DataIngestion(data_ingestion_config)
    data_ingestion_artifact = ingestion.initiate_data_ingestion()
    data_validation_config = DataValidationConfig(data_ingestion_config)
    validation = DataValidation(data_validation_config,data_ingestion_artifact,data_ingestion_config)
    data_validation_artifact = validation.initiate_data_validation()
    data_transformation_config = DataTransformationConfig(data_validation_config=data_validation_config)
    transformation = DataTransformation(data_validation_artifact, data_transformation_config)
    data_transformation_artifact = transformation.initialise_data_transformation()
    
    
    
