from datetime import datetime
from pydantic import BaseModel

class Note(BaseModel):
    created_at: datetime
    description: str