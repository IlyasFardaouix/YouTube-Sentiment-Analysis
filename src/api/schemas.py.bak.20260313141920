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
    text: str  # Ajout du texte pour l'affichage
    sentiment: int  # -1 (négatif), 0 (neutre), 1 (positif)
    confidence: float

class BatchPredictionResponse(BaseModel):
    predictions: List[Prediction]
    stats: dict
