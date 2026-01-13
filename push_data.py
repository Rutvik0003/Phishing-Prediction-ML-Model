import os
import sys
from src.exception import CustomException

from dotenv import load_dotenv
load_dotenv()

try:
    MONGODB_URL = os.getenv('MONGODB_URL')
    print(MONGODB_URL)
except Exception as e:
    raise CustomException(e)