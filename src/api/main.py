from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.api.schemas import CommentBatch, BatchPredictionResponse, Prediction
from src.api.prediction import ModelService
import uvicorn

# Create FastAPI application
app = FastAPI(
    title="YouTube Sentiment Analysis API",
    description="API to analyze sentiment of YouTube comments",
    version="1.0.0",
)

# CORS configuration to allow Chrome extension
# TODO: In production, limit allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For now allow all for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model service (loads on startup)
model_service = ModelService()


@app.get("/health")
async def health_check():
    """
    Endpoint to check if API is working and model is loaded
    """
    status = "healthy" if model_service.model else "unhealthy"
    return {"status": status, "model_loaded": model_service.model is not None}


@app.post("/predict_batch", response_model=BatchPredictionResponse)
async def predict_batch(batch: CommentBatch):
    """
    Predicts sentiment for a batch of comments
    Returns predictions and statistics
    """
    # Check if model is loaded
    if not model_service.model:
        raise HTTPException(
            status_code=503, detail="Model not loaded. Please train the model first."
        )

    # Case where there are no comments
    if not batch.comments or len(batch.comments) == 0:
        return BatchPredictionResponse(
            predictions=[],
            stats={
                "total": 0,
                "positive": 0,
                "neutral": 0,
                "negative": 0,
                "positive_pct": 0,
                "neutral_pct": 0,
                "negative_pct": 0,
            },
        )

    # Extract texts and IDs
    texts = [c.text for c in batch.comments]
    ids = [c.id for c in batch.comments]

    try:
        # Make predictions
        preds, confs = model_service.predict_batch(texts)

        # Build response
        predictions = []
        sentiment_counts = {-1: 0, 0: 0, 1: 0}  # negative, neutral, positive

        for i, (pred, conf) in enumerate(zip(preds, confs)):
            pred_int = int(pred)
            predictions.append(
                Prediction(
                    id=ids[i],
                    text=texts[i],  # Include text for display in extension
                    sentiment=pred_int,
                    confidence=float(conf),
                )
            )
            sentiment_counts[pred_int] += 1

        # Calculate statistics
        total = len(predictions)
        stats = {
            "total": total,
            "positive": sentiment_counts[1],
            "neutral": sentiment_counts[0],
            "negative": sentiment_counts[-1],
            "positive_pct": (
                round(sentiment_counts[1] / total * 100, 1) if total > 0 else 0
            ),
            "neutral_pct": (
                round(sentiment_counts[0] / total * 100, 1) if total > 0 else 0
            ),
            "negative_pct": (
                round(sentiment_counts[-1] / total * 100, 1) if total > 0 else 0
            ),
        }

        return BatchPredictionResponse(predictions=predictions, stats=stats)

    except Exception as e:
        # Basic error handling
        print(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


if __name__ == "__main__":
    # To run locally
    uvicorn.run(app, host="0.0.0.0", port=8000)
