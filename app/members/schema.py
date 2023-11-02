from app.base import CamelModel
from typing import Optional
from pydantic import Field
import uuid

class UserSchema(CamelModel):
    """User schema"""
    id: Optional[str] = Field(default_factory=lambda: uuid.uuid4().__str__())
    username: str
    email: str
    cpf: str