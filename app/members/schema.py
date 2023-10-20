from app.base import CamelModel
import uuid

class UserSchema(CamelModel):
    """User schema"""
    id: str = uuid.uuid4()
    username: str
    email: str
    cpf: str