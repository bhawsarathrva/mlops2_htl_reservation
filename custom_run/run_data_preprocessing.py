#!/usr/bin/env python
"""
Standalone Data Preprocessing Script
This script can be run from anywhere and will work correctly.
"""
import sys
import os
from pathlib import Path

# Add the PROJECT CODE directory to Python path
PROJECT_ROOT = Path(__file__).parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

# Now we can import from src
from src.data_preprocessing import DataProcessor
from config.paths_config import TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH

if __name__ == "__main__":
    print("=" * 60)
    print("Hotel Reservation Prediction - Data Preprocessing")
    print("=" * 60)
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Train Data: {TRAIN_FILE_PATH}")
    print(f"Test Data: {TEST_FILE_PATH}")
    print("=" * 60)
    
    processor = DataProcessor(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)
    processor.process()
    
    print("=" * 60)
    print("Data Preprocessing Complete!")
    print("=" * 60)
