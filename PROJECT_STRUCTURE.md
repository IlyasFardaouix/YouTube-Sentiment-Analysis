# Project Structure

This document describes the organization of the YouTube Sentiment Analysis project.

## 📁 File Organization

```
YouTube-Sentiment-Analysis/
│
├── src/                          # Main source code
│   ├── api/                      # FastAPI
│   │   ├── main.py              # API entry point
│   │   ├── prediction.py        # Prediction service
│   │   └── schemas.py           # Pydantic models
│   │
│   ├── data/                    # Data processing
│   │   ├── download_data.py     # Dataset download
│   │   └── process_data.py      # Cleaning and preparation
│   │
│   └── models/                   # ML models
│       └── train_model.py       # Training script
│
├── chrome-extension/             # Chrome extension
│   ├── manifest.json            # Extension configuration
│   ├── popup.html               # User interface
│   ├── popup.js                 # Extension logic
│   ├── content.js               # Script injected into YouTube
│   └── style.css                # CSS styles
│
├── data/                        # Data (gitignored)
│   ├── raw/                     # Raw data
│   └── processed/              # Processed data
│
├── models/                      # Trained models (gitignored)
│   └── sentiment_model.joblib  # Saved model
│
├── logs/                        # Logs (optional)
│
├── app.py                       # Entry point for Hugging Face
├── setup.py                     # Initialization script
├── run_pipeline.py              # Script to run complete pipeline
├── test_api.py                  # API tests
├── config.py                    # Project configuration
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
└── README.md                    # Main documentation
```

## 🔄 Project Workflow

1. **Data Download** (`src/data/download_data.py`)
   - Downloads Reddit dataset from GitHub

2. **Data Processing** (`src/data/process_data.py`)
   - Cleans text
   - Splits into train/test

3. **Training** (`src/models/train_model.py`)
   - Trains a Logistic Regression model with GridSearch
   - Saves the model

4. **API** (`src/api/main.py`)
   - Exposes the model via FastAPI
   - `/predict_batch` endpoint to analyze comments

5. **Chrome Extension**
   - Extracts YouTube comments
   - Sends to API
   - Displays results

## 🚀 Useful Commands

```bash
# Initial setup
python setup.py

# Complete pipeline
python run_pipeline.py

# Or step by step:
python src/data/download_data.py
python src/data/process_data.py
python src/models/train_model.py

# Run API
python -m uvicorn src.api.main:app --reload

# Test API
python test_api.py
```

## 📝 Notes

- The `data/` and `models/` folders are in `.gitignore` (files too large)
- Use `.gitkeep` to maintain structure in Git
- The model must be present for the API to work
