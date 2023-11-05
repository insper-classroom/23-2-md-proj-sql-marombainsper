from typing import List

from fastapi import APIRouter, HTTPException
from .schema import SubscribeSchema
from fastapi import APIRouter, HTTPException, Depends
from app.base import CamelModel
from ..members.schema import MemberSchema
from app.db import get_db, Session
from .service import SubscriptionsService


router = APIRouter()

@router.get('/', response_model=List[SubscribeSchema])
async def get_subscribe(session: Session = Depends(get_db)):
    """Get all subscribe"""
    return await SubscriptionsService.get_all(session)

@router.post('/', response_model=SubscribeSchema)
async def create_subscribe(subscribe: SubscribeSchema, session: Session = Depends(get_db)):
    """Create a new subscribe"""
    resp = await SubscriptionsService.create_subscription(subscribe, session)
    if resp:
        return resp
    else:
        raise HTTPException(status_code=400, detail="Subscription not created")

@router.get('/{subscribe_id}', response_model=SubscribeSchema)
async def show_subscribe(subscribe_id: str, session: Session = Depends(get_db)):
    """Show a subscription by id"""

    subscription = await SubscriptionsService.show_subscription(subscribe_id, session)
    if subscription:
        return subscription
    else:
        raise HTTPException(status_code=404, detail="Subscription not found")

@router.put('/{subscribe_id}', response_model=SubscribeSchema)
async def update_subscribe(subscribe_id: str, subscribe: SubscribeSchema, session: Session = Depends(get_db)):
    """Update a subscribe by id"""

    try:
        subscription = await SubscriptionsService.update_subscription(subscribe_id, subscribe, session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    if subscription:
        return subscription
    else:
        raise HTTPException(status_code=404, detail="Subscription not found")

@router.delete('/{subscribe_id}', response_model=SubscribeSchema)
async def delete_subscribe(subscribe_id: str, session: Session = Depends(get_db)):
    """Delete a subscribe by id"""

    subscription = await SubscriptionsService.delete_subscription(subscribe_id, session)
    if subscription:
        return subscription
    else:
        raise HTTPException(status_code=404, detail="Subscription not found")