FROM python:3.10-slim

WORKDIR /app

# Install system dependencies if needed
# (not really necessary for this project but good to know)

# Copy requirements.txt first to optimize Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create necessary directories (just in case)
RUN mkdir -p data/raw data/processed models logs

# Note: The model must be present in the models/ folder
# For Hugging Face Spaces, you need to either:
# 1. Commit the model (not ideal as it's a large file)
# 2. Download it during build (better solution)
# 3. Train it during build (too long)

# Expose port (7860 for Hugging Face Spaces)
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]
