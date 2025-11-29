from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime
from uuid import uuid4, UUID

class TodoCreate(BaseModel):
    title: str
    details: str
    priority: Literal[1, 2, 3] = 3
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Optional[datetime]
    is_completed: bool = False


class TodoResponse(TodoCreate):
    id: UUID = Field(default_factory=uuid4)

    class Config:
        from_attributes = True