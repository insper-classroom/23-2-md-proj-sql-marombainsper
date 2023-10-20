from app.db import get_db, Session
from typing import List

from .schema import UserSchema

class UserService:
    @staticmethod
    async def get_all(session: Session) -> List[UserSchema]:
        resp = session.query(UserSchema).all()

        return [UserSchema(**i.__dict__) for i in resp]