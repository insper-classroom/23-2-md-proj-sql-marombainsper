from app.base import CamelModel
from typing import Optional
from pydantic import Field
import uuid

class SubscribeSchema(CamelModel):
    """Subscribe schema"""
    id: Optional[str] = Field(default_factory=lambda: uuid.uuid4().__str__())
    id_user: str
    id_plan: str
