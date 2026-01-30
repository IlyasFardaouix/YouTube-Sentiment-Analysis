import joblib
import os
import numpy as np
from pathlib import Path

class ModelService:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        # Get the project root directory (parent of src)
        project_root = Path(__file__).parent.parent.parent
        model_path = project_root / "models" / "sentiment_model.joblib"
        
        # Also try relative path in case we're running from project root
        if not model_path.exists():
            model_path = Path("models") / "sentiment_model.joblib"
        
        if model_path.exists():
            try:
                self.model = joblib.load(str(model_path))
                print(f"Model loaded successfully from {model_path}")
            except Exception as e:
                print(f"Error loading model: {e}")
                self.model = None
        else:
            print(f"Model not found at {model_path}")
            print("Please train the model first using: python src/models/train_model.py")

    def predict_batch(self, texts):
        if not self.model:
            raise Exception("Model not loaded. Please train the model first.")
        
        # Convert to list if needed
        if isinstance(texts, str):
            texts = [texts]
        
        # Predict class (-1, 0, or 1)
        predictions = self.model.predict(texts)
        
        # Get probabilities for confidence score
        probas = self.model.predict_proba(texts)
        # Take max probability as confidence
        confidences = np.max(probas, axis=1)
        
        return predictions, confidences
