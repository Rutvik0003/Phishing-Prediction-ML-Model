import os
import sys
import dill
import yaml

import numpy as np
import pickle

from src.exception import CustomException
from src.logger import logging
from typing import Dict

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


def save_pickle_obj(obj, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)