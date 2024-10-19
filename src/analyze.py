# src/analyze.py
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_data(df: pd.DataFrame):
    try:
        logger.info("Starting data analysis")
        
        # Example Insights:
        # 1. Total Sales per Category
        sales_per_category = df.groupby('Category')['Amount'].sum().reset_index()
        logger.info("Total Sales per Category:\n" + sales_per_category.to_string())
        
        # 2. Sales Over Time
        sales_over_time = df.groupby('Date')['Amount'].sum().reset_index()
        logger.info("Sales Over Time:\n" + sales_over_time.to_string())
        
        # 3. Top 10 Products by Sales
        top_products = df.groupby('SKU')['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False).head(10)
        logger.info("Top 10 Products by Sales:\n" + top_products.to_string())
        
        # Additional insights can be added here
    except Exception as e:
        logger.error(f"Error in analyze_data: {e}")
        raise
