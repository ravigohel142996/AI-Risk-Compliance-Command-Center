"""
Data loading and preprocessing module
"""
import pandas as pd
from pathlib import Path
from typing import Optional
from src.utils.config import DATA_DIR
from src.utils.logger import app_logger


class DataLoader:
    """Handle data loading and preprocessing"""
    
    def __init__(self, data_dir: Path = DATA_DIR):
        self.data_dir = data_dir
        self.logger = app_logger
        
    def load_csv(self, filename: str) -> Optional[pd.DataFrame]:
        """
        Load CSV file from data directory
        
        Args:
            filename: Name of CSV file
            
        Returns:
            DataFrame or None if file not found
        """
        file_path = self.data_dir / filename
        
        try:
            if file_path.exists():
                df = pd.read_csv(file_path)
                self.logger.info(f"Loaded {len(df)} records from {filename}")
                return df
            else:
                self.logger.warning(f"File not found: {file_path}")
                return None
        except Exception as e:
            self.logger.error(f"Error loading {filename}: {str(e)}")
            return None
    
    def save_csv(self, df: pd.DataFrame, filename: str) -> bool:
        """
        Save DataFrame to CSV file
        
        Args:
            df: DataFrame to save
            filename: Output filename
            
        Returns:
            True if successful, False otherwise
        """
        file_path = self.data_dir / filename
        
        try:
            df.to_csv(file_path, index=False)
            self.logger.info(f"Saved {len(df)} records to {filename}")
            return True
        except Exception as e:
            self.logger.error(f"Error saving {filename}: {str(e)}")
            return False
    
    def validate_data(self, df: pd.DataFrame, required_columns: list) -> bool:
        """
        Validate that DataFrame has required columns
        
        Args:
            df: DataFrame to validate
            required_columns: List of required column names
            
        Returns:
            True if valid, False otherwise
        """
        missing = set(required_columns) - set(df.columns)
        if missing:
            self.logger.error(f"Missing required columns: {missing}")
            return False
        return True
