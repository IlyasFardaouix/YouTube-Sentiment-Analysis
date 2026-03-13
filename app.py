"""
Main entry point for the application
Used for deployment on Hugging Face Spaces (port 7860)
"""

from src.api.main import app
import uvicorn

if __name__ == "__main__":
    # Port 7860 for Hugging Face Spaces
    uvicorn.run(app, host="0.0.0.0", port=7860)
