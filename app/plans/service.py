from app.db import Session
from typing import List
from sqlalchemy.orm import joinedload
from .schema import PlansSchema
from .model import Plan
from app.subscriptions.model import Subscription
from app.members.schema import MemberSchema


class PlansService:
    @staticmethod
    async def get_all(session: Session) -> List[PlansSchema]:
        resp = session.query(Plan).all()

        return [PlansSchema(**i.__dict__) for i in resp]
    
    @staticmethod
    async def create(new_plan: PlansSchema, session: Session) -> PlansSchema:
        new_user = Plan(**new_plan.model_dump())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return PlansSchema(**new_user.__dict__)
    
    @staticmethod
    async def show_plan(plan_id: str, session: Session) -> PlansSchema:
        resp = session.query(Plan).filter(Plan.id == plan_id).first()
        if resp:
            return PlansSchema(**resp.__dict__)
        else:
            return None
    
    @staticmethod
    async def update_plan(plan_id: str, plan: PlansSchema, session: Session) -> PlansSchema:
        existing_plan = session.query(Plan).filter(Plan.id == plan_id).first()
        if existing_plan:
            for field, value in plan.model_dump().items():
                if field != "id":
                    setattr(existing_plan, field, value)
            session.commit()
            session.refresh(existing_plan)
            return PlansSchema(**existing_plan.__dict__)
        else:
            return None
    
    @staticmethod
    async def delete_plan(plan_id: str, session: Session) -> PlansSchema:
        resp = session.query(Plan).filter(Plan.id == plan_id).first()
        if resp:
            session.delete(resp)
            session.commit()
            return PlansSchema(**resp.__dict__)
        else:
            return None
        
    @staticmethod
    async def get_members_of_plan(plan_id: str, session: Session) -> List[MemberSchema]:
        resp = session.query(Subscription).options(joinedload(Subscription.user)).filter(Subscription.id_plan == plan_id).all()
        if resp:
            return [MemberSchema(**i.user.__dict__) for i in resp]
        else:
            return None