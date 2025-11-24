from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.api.schemas import CommentBatch, BatchPredictionResponse, Prediction
from src.api.prediction import ModelService
import uvicorn

app = FastAPI(title="YouTube Sentiment Analysis API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for extension
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model service
model_service = ModelService()

@app.get("/health")
async def health_check():
    status = "healthy" if model_service.model else "unhealthy"
    return {"status": status, "model_loaded": model_service.model is not None}

@app.post("/predict_batch", response_model=BatchPredictionResponse)
async def predict_batch(batch: CommentBatch):
    if not model_service.model:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    if not batch.comments:
        return BatchPredictionResponse(predictions=[], stats={})
    
    texts = [c.text for c in batch.comments]
    ids = [c.id for c in batch.comments]
    
    try:
        preds, confs = model_service.predict_batch(texts)
        
        predictions = []
        sentiment_counts = {-1: 0, 0: 0, 1: 0}
        
        for i, (pred, conf) in enumerate(zip(preds, confs)):
            predictions.append(Prediction(
                id=ids[i],
                sentiment=int(pred),
                confidence=float(conf)
            ))
            sentiment_counts[int(pred)] += 1
            
        total = len(predictions)
        stats = {
            "total": total,
            "positive": sentiment_counts[1],
            "neutral": sentiment_counts[0],
            "negative": sentiment_counts[-1],
            "positive_pct": round(sentiment_counts[1] / total * 100, 1) if total > 0 else 0,
            "neutral_pct": round(sentiment_counts[0] / total * 100, 1) if total > 0 else 0,
            "negative_pct": round(sentiment_counts[-1] / total * 100, 1) if total > 0 else 0,
        }
        
        return BatchPredictionResponse(predictions=predictions, stats=stats)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
