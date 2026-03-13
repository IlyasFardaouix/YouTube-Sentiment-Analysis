```python
from pydantic import BaseModel
from typing import List, Optional, Dict

class Comment(BaseModel):
    """
    Represents a comment with its attributes.
    
    Attributes:
    id (str): Unique identifier for the comment.
    text (str): The text content of the comment.
    author (Optional[str]): The author of the comment. Defaults to None.
    timestamp (Optional[str]): The timestamp of the comment. Defaults to None.
    """
    id: str
    text: str
    author: Optional[str] = None
    timestamp: Optional[str] = None

class CommentBatch(BaseModel):
    """
    Represents a batch of comments.
    
    Attributes:
    comments (List[Comment]): A list of comments.
    """
    comments: List[Comment]

class Prediction(BaseModel):
    """
    Represents a sentiment prediction result.
    
    Attributes:
    id (str): Unique identifier for the prediction.
    text (str): The text content of the prediction for display.
    sentiment (int): The sentiment score (-1 for negative, 0 for neutral, 1 for positive).
    confidence (float): The confidence level of the prediction.
    """
    id: str
    text: str
    sentiment: int  # -1 (négatif), 0 (neutre), 1 (positif)
    confidence: float

class BatchPredictionResponse(BaseModel):
    """
    Represents the response for a batch prediction.
    
    Attributes:
    predictions (List[Prediction]): A list of prediction results.
    stats (Dict): Additional statistics for the prediction.
    """
    predictions: List[Prediction]
    stats: Dict
```