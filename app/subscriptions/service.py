from app.db import Session
from typing import List
from sqlalchemy.orm import joinedload
from .schema import SubscribeSchema
from .model import Subscription
from app.plans.schema import PlansSchema
from app.members.schema import MemberSchema


class SubscriptionsService:
    @staticmethod
    async def get_all(session: Session) -> List[SubscribeSchema]:
        resp = session.query(Subscription).all()
        return [SubscribeSchema(**subscription.__dict__) for subscription in resp]

    @staticmethod
    async def show_subscription(subscription_id: str, session: Session) -> SubscribeSchema:
        resp = session.query(Subscription).filter(Subscription.id == subscription_id).first()
        if resp:
            return SubscribeSchema(**resp.__dict__)
        else:
            return None
        
    @staticmethod
    async def create_subscription(subscription: SubscribeSchema, session: Session) -> SubscribeSchema:
        new_subscription = Subscription(**subscription.model_dump())
        session.add(new_subscription)
        session.commit()
        session.refresh(new_subscription)
        return SubscribeSchema(**new_subscription.__dict__)

    @staticmethod
    async def update_subscription(subscription_id: str, subscription: SubscribeSchema, session: Session) -> SubscribeSchema:
        existing_subscription = session.query(Subscription).filter(Subscription.id == subscription_id).first()
        if existing_subscription:
            for field, value in subscription.model_dump(exclude_unset=True).items():
                if field != "id":
                    setattr(existing_subscription, field, value)
            session.commit()

            updated_subscription_dict = {c.name: getattr(existing_subscription, c.name) for c in existing_subscription.__table__.columns}
            return SubscribeSchema(**updated_subscription_dict)
        else:
            return None

    @staticmethod
    async def delete_subscription(subscription_id: str, session: Session) -> SubscribeSchema:
        resp = session.query(Subscription).filter(Subscription.id == subscription_id).first()
        if resp:
            session.delete(resp)
            session.commit()
            return SubscribeSchema(**resp.__dict__)
        else:
            return None
