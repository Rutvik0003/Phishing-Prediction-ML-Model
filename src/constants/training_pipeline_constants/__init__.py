PIPELINE_NAME: str = "PhishingPredictionTrainingPipeline"
ARTIFACT_PATH: str = "artifacts"

INGESTION_FOLDER: str = "ingestion"
FEATURE_FOLDER: str = "feature"

RAW_DATA_PATH: str = "artifacts/ingestion/raw_data.csv"
TRAIN_DATA_PATH: str = "artifacts/ingestion/train.csv"
TEST_DATA_PATH: str = "artifacts/ingestion/test.csv"

TRAIN_TEST_SPLIT_RATIO: float = 0.3

DATABASE_NAME: str = "phishingdb"
COLLECTION_NAME: str = "phishing_collection"
