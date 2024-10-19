# src/extract.py
import pandas as pd
import os
from dotenv import load_dotenv
import logging

load_dotenv(dotenv_path=os.path.join('config', '.env'))

logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger(__name__)

def extract_data(file_path: str) -> pd.DataFrame:
    try:
        logger.info(f"Extracting data from {file_path}")
        df = pd.read_csv(file_path, encoding='utf-8')
        logger.info(f"Extracted {len(df)} records")
        return df
    except Exception as e:
        logger.error(f"Error in extract_data: {e}")
        raise
