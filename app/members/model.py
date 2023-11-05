from sqlalchemy import Integer, Column, String, VARCHAR
from app.db import Base
from sqlalchemy.orm import relationship

from .schema import MemberSchema

class Member(Base):
    __tablename__ = "members"

    id = Column(VARCHAR(60), primary_key=True, index=True)
    username = Column(VARCHAR(30), unique=True, index=True)
    cpf = Column(VARCHAR(11), unique=True, index=True)
    email = Column(VARCHAR(50), unique=True, index=True)

    subscriptions = relationship('Subscription', back_populates='user', overlaps='user')


    def update(self, changes: MemberSchema):
      for key, val in changes.model_dump().items():
        setattr(self, key, val)
      return self