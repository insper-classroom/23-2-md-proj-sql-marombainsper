from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base 
from app.members.model import Member

class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(VARCHAR(60), primary_key=True)
    id_user = Column(VARCHAR(60), ForeignKey('members.id'), nullable=False)
    id_plan = Column(VARCHAR(60), ForeignKey('plans.id'), nullable=False)
    
    # Define relationships with `back_populates` and specify `overlaps` where necessary
    plan = relationship("Plan", back_populates="subscriptions", overlaps="subscriptions")
    user = relationship("Member", back_populates="subscriptions", overlaps="subscriptions")
