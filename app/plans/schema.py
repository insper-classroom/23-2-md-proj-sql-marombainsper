from app.base import CamelModel
import uuid

class PlansSchema(CamelModel):
    """User schema"""
    id: str = uuid.uuid4()
    type: str
    price: float
    