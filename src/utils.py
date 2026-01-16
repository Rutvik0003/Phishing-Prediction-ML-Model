import os
import sys
import dill
import yaml

from src.exception import CustomException
from src.logger import logging

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