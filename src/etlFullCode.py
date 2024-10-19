import pandas as pd
import boto3
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv(dotenv_path=os.path.join('config', '.env'))

# Set up logging
logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger(__name__)

def extract_data(file_path: str) -> pd.DataFrame:
    """Extract data from a CSV file."""
    try:
        logger.info(f"Extracting data from {file_path}")
        df = pd.read_csv(file_path, encoding='utf-8')
        logger.info(f"Extracted {len(df)} records")
        return df
    except Exception as e:
        logger.error(f"Error in extract_data: {e}")
        raise

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Transform the data by removing duplicates and converting date columns."""
    try:
        logger.info("Starting data transformation")
        
        # Remove duplicates
        initial_count = len(df)
        df = df.drop_duplicates()
        final_count = len(df)
        logger.info(f"Removed {initial_count - final_count} duplicate records")
        
        # Convert 'Date' column to datetime
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            logger.info("Converted 'Date' column to datetime")
        
        # Any additional transformations can be added here
        
        logger.info(f"Data shape after transformation: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error in transform_data: {e}")
        raise

def upload_to_s3(df: pd.DataFrame, bucket_name: str, file_name: str):
    """Upload the DataFrame to an S3 bucket."""
    try:
        logger.info(f"Uploading {file_name} to S3 bucket: {bucket_name}")
        s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        
        # Convert DataFrame to CSV in memory
        csv_buffer = df.to_csv(index=False)
        
        # Upload file to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=csv_buffer,
            ContentType='text/csv'  # Specify content type if known
        )
        
        logger.info("Upload successful")
    
    except Exception as e:
        logger.error(f"Error in upload_to_s3: {e}")
        raise

if __name__ == "__main__":
    # File path for the source data
    file_path = "data\\raw\\Amazon Sale Report.csv"  # Update this path to your actual file location
    
    # Step 1: Extract data
    try:
        extracted_data = extract_data(file_path)
        logger.info("Data extraction successful")
    except Exception as e:
        logger.error(f"Failed to extract data: {e}")
        exit(1)
    
    # Step 2: Transform data
    try:
        transformed_data = transform_data(extracted_data)
        logger.info("Data transformation successful")
    except Exception as e:
        logger.error(f"Failed to transform data: {e}")
        exit(1)
    
    # Step 3: Upload to S3
    bucket_name = 'examplebucneonman'  # Replace with your S3 bucket name
    file_name = 'transformed_Amazon_Sales_Data.csv'
    
    try:
        upload_to_s3(transformed_data, bucket_name, file_name)
        logger.info("ETL process completed successfully")
    except Exception as e:
        logger.error(f"Failed to upload data to S3: {e}")
        exit(1)
