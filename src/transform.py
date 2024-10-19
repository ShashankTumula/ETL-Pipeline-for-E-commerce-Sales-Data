# src/transform.py
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        logger.info("Starting data transformation")
        
        # Remove duplicate records
        initial_count = len(df)
        df = df.drop_duplicates()
        final_count = len(df)
        logger.info(f"Removed {initial_count - final_count} duplicate records")
        
        # Handle missing values (example: drop rows with any missing values)
        df = df.dropna()
        logger.info(f"Data shape after dropping missing values: {df.shape}")
        
        # Additional transformations can be added here
        # Example: Convert 'Date' column to datetime
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            logger.info("Converted 'Date' column to datetime")
        
        return df
    except Exception as e:
        logger.error(f"Error in transform_data: {e}")
        raise
