from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: str
    text: str
    author: Optional[str] = None
    timestamp: Optional[str] = None

class CommentBatch(BaseModel):
    comments: List[Comment]

class Prediction(BaseModel):
    id: str
    sentiment: int  # -1, 0, 1
    confidence: float

class BatchPredictionResponse(BaseModel):
    predictions: List[Prediction]
    stats: dict
