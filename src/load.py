# src/load.py
import pandas as pd
import boto3
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

load_dotenv(dotenv_path=os.path.join('config', '.env'))

logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger(__name__)

def upload_to_s3(df: pd.DataFrame, bucket_name: str, file_name: str):
    try:
        logger.info(f"Uploading {file_name} to S3 bucket: {bucket_name}")
        s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        # Convert DataFrame to CSV in memory
        csv_buffer = df.to_csv(index=False)
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer)
        logger.info("Upload successful")
    except Exception as e:
        logger.error(f"Error in upload_to_s3: {e}")
        raise
