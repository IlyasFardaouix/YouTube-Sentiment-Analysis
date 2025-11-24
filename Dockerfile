FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to leverage cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create directories if they don't exist (though COPY . . should handle it if they exist locally)
# But we need to make sure models are there. 
# Note: In a real scenario, models might be pulled from DVC or similar, 
# but for this TP we assume they are committed or copied.
# The .gitignore ignores models/ but we need the model for the image.
# We should probably un-ignore the model for the deployment or copy it explicitly.
# Or the user will upload it to HF Space.
# For Dockerfile, we assume the model is in the context.

# Expose the port
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]
