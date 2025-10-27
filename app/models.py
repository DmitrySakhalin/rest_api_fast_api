from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field

class Advertisement(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., max_length=100)
    description: str
    price: float
    author: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
