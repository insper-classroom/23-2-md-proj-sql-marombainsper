from app.db import get_db, Session
from typing import List

from .schema import MemberSchema
from .model import Member

class UserService:
    @staticmethod
    async def get_all(session: Session) -> List[MemberSchema]:
        resp = session.query(Member).all()

        return [MemberSchema(**i.__dict__) for i in resp]
    
    @staticmethod
    async def create(new_member: MemberSchema, session: Session) -> MemberSchema:
        new_user = Member(**new_member.model_dump())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return MemberSchema(**new_user.__dict__)
    
    @staticmethod
    async def show_member(member_id: str, session: Session) -> MemberSchema:
        resp = session.query(Member).filter(Member.id == member_id).first()
        if resp:
            return MemberSchema(**resp.__dict__)
        else:
            return None
        
    @staticmethod
    async def update_member(member_id: str, member: MemberSchema, session: Session) -> MemberSchema:
        existing_member = session.query(Member).filter(Member.id == member_id).first()
        if existing_member:
            for field, value in member.model_dump().items():
                if field != "id":
                    setattr(existing_member, field, value)

            session.commit()

            session.refresh(existing_member)

            return MemberSchema(**existing_member.__dict__)
        else:
            return None
        
    @staticmethod
    async def delete_member(member_id: str, session: Session) -> MemberSchema:
        resp = session.query(Member).filter(Member.id == member_id).first()
        if resp:
            session.delete(resp)
            session.commit()
            return MemberSchema(**resp.__dict__)
        else:
            return None