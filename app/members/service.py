from app.db import get_db, Session
from typing import List

from .schema import UserSchema
from .model import Member

import uuid
class UserService:
    @staticmethod
    async def get_all(session: Session) -> List[UserSchema]:
        resp = session.query(UserSchema).all()

        return [UserSchema(**i.__dict__) for i in resp]
    
    @staticmethod
    async def create(new_member: UserSchema, session: Session) -> UserSchema:
        new_user = Member(**new_member.model_dump())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return UserSchema(**new_user.__dict__)