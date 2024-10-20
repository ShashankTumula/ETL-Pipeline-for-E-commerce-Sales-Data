# main.py
import os
import logging
from datetime import datetime
from src.extract import extract_data
from src.transform import transform_data
from src.load import upload_to_s3
from src.analyze import analyze_data
from dotenv import load_dotenv

def setup_logging():
    load_dotenv(dotenv_path=os.path.join('config', '.env'))
    logging.basicConfig(
        level=os.getenv('LOG_LEVEL', 'INFO'),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Paths and configurations
        raw_data_path = os.path.join('data', 'raw', 'Amazon Sale Report.csv')
        processed_data_path = os.path.join('data', 'processed', 'cleaned_sales_data.csv')
        bucket_name = os.getenv('S3_BUCKET_NAME')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        s3_file_name = f"cleaned_sales_data_{timestamp}.csv"
        
        # ETL Steps
        df = extract_data(raw_data_path)
        df_cleaned = transform_data(df)
        upload_to_s3(df_cleaned, bucket_name, s3_file_name)
        analyze_data(df_cleaned)  # Optional: Perform analysis
        
        logger.info("ETL pipeline executed successfully")
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")

if __name__ == "__main__":
    main()
