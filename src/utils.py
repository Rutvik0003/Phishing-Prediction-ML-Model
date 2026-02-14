import os
import sys
import dill
import yaml

import numpy as np
import pickle

from src.exception import CustomException
from src.logger import logging
from typing import Dict

from src.entity.artifact_entity import ClassificationMatricArtifact

from sklearn.metrics import accuracy_score, precision_score, recall_score


class TrainingModel:
    def __init__(self, preprocessor, model):
        self.preprocessor = preprocessor
        self.model = model

    def predict(self,x):
        x_transformed = self.preprocessor.transform(x)
        y_pred = self.model.predict(x_transformed)

        return y_pred



def read_yaml(filepath: str) -> Dict:
    try:
        with open(filepath, "r") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise CustomException(e, sys)

def write_yaml(filepath: str, data: Dict) -> None:
    try:
        with open(filepath, "w") as yaml_file:
            yaml.dump(
                data,
                yaml_file,
                default_flow_style=False,
                sort_keys=False
            )

    except Exception as e:
        raise CustomException(e, sys)
    
def save_numpy_obj(obj, file_path):

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    np.save(file_path, obj)

def load_numpy_obj(file_path: str):
    try:
        return np.load(file_path, allow_pickle=True)

    except Exception as e:
        raise CustomException(e, sys)


def save_pickle_obj(obj, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)

def load_pickle_obj(file_path: str):
    
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def get_classification_matric(y_true, y_pred):
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    accuracy = accuracy_score(y_true, y_pred)

    classification_matric_artifact = ClassificationMatricArtifact(
        precision= precision,
        recall= recall,
        accuracy= accuracy
    )

    return classification_matric_artifact
    