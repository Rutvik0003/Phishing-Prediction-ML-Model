from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_data_path : str
    test_data_path : str

@dataclass
class DataValidationArtifact:
    is_drift_found : bool
    train_data_validation_status : bool
    test_data_validation_status:bool
    valid_train_data_path : str
    invalid_train_data_path : str
    valid_test_data_path : str
    invalid_test_data_path : str
