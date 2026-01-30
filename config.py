"""
Configuration file for the project
Contains constants and parameters used in the project
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# Data files
RAW_DATA_FILE = RAW_DATA_DIR / "reddit.csv"
TRAIN_FILE = PROCESSED_DATA_DIR / "train.csv"
TEST_FILE = PROCESSED_DATA_DIR / "test.csv"

# Model
MODEL_FILE = MODELS_DIR / "sentiment_model.joblib"

# API Configuration
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
HF_PORT = 7860  # Port for Hugging Face Spaces

# URLs
REDDIT_DATASET_URL = "https://raw.githubusercontent.com/Himanshu-1703/reddit-sentiment-analysis/refs/heads/main/data/reddit.csv"
# TODO: Update with your Hugging Face URL
HF_SPACE_URL = "https://has1elb-youtube-sentiment-analysis.hf.space"

# Model parameters
MAX_FEATURES = 5000
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Chrome Extension
MAX_COMMENTS = 50  # Maximum number of comments to analyze
