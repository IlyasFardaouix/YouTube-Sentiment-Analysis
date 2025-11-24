# YouTube Sentiment Analysis MLOps Project

[![GitHub](https://img.shields.io/badge/GitHub-TALEB7-blue)](https://github.com/TALEB7/YouTube-Sentiment-Analysis)

## Description

This project implements a complete MLOps pipeline for analyzing the sentiment of YouTube comments. It consists of a Machine Learning model trained on Reddit data, a FastAPI backend, and a Chrome Extension for the user interface.

## Architecture

- **ML Engine**: Logistic Regression with TF-IDF, trained on Reddit Sentiment dataset.
- **Backend**: FastAPI serving the model with `/predict_batch` endpoint.
- **Frontend**: Chrome Extension injecting content scripts to extract comments and displaying analysis in a popup.
- **Deployment**: Dockerized application ready for Hugging Face Spaces.

## Installation

### Prerequisites

- Python 3.10+
- Google Chrome
- Git

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/TALEB7/YouTube-Sentiment-Analysis.git
   cd YouTube-Sentiment-Analysis
   ```
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Train the model (if not already trained):
   ```bash
   python src/data/download_data.py
   python src/data/process_data.py
   python src/models/train_model.py
   ```
5. Run the API:
   ```bash
   python -m uvicorn src.api.main:app --reload
   ```

### Chrome Extension Setup

1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable "Developer mode" (top right).
3. Click "Load unpacked".
4. Select the `chrome-extension` folder in this project.

## Usage

1. Ensure the API is running (locally or on Hugging Face).
2. Go to a YouTube video page.
3. Scroll down to load some comments.
4. Click the extension icon.
5. Click "Analyze Comments".
6. View the sentiment distribution and individual comment analysis.

## Deployment

To deploy on Hugging Face Spaces:

1. Create a new Space (SDK: Docker).
2. Upload the contents of this repository (ensure `models/sentiment_model.joblib` is included).
3. The Space will build and run the API.
4. Update the `apiUrl` in `chrome-extension/popup.js` to your Space URL.

## Author
- TALEB Sami

