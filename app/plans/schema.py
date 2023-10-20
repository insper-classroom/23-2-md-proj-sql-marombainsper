from app.base import CamelModel
import uuid

class PlansSchema(CamelModel):
    """User schema"""
    id: str = uuid.uuid4()
    price: float
    