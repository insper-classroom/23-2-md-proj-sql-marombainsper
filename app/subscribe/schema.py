from app.base import CamelModel
import uuid

class SubscribeSchema(CamelModel):
    """Subscribe schema"""
    id_subscribe: str = uuid.uuid4()
    id_user: str = uuid.uuid4()
    id_plan: str = uuid.uuid4()
