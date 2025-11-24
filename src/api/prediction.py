import joblib
import os
import numpy as np

class ModelService:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        model_path = os.path.join("models", "sentiment_model.joblib")
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
            print("Model loaded successfully.")
        else:
            print(f"Model not found at {model_path}")

    def predict_batch(self, texts):
        if not self.model:
            raise Exception("Model not loaded")
        
        # Predict class
        predictions = self.model.predict(texts)
        # Predict probabilities
        probas = self.model.predict_proba(texts)
        # Get max probability as confidence
        confidences = np.max(probas, axis=1)
        
        return predictions, confidences
