from app.db import Base
from sqlalchemy import Float, Column, String, VARCHAR
from sqlalchemy.orm import relationship
from app.subscriptions.model import Subscription

class Plan(Base):
    __tablename__ = "plans"

    id = Column(VARCHAR(60), primary_key=True, index=True)
    type = Column(VARCHAR(30), unique=True)
    price = Column(Float)

    subscriptions = relationship("Subscription", back_populates="plan", overlaps="plan")

