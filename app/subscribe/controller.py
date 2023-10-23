from typing import List

from fastapi import APIRouter, HTTPException
from .schema import SubscribeSchema
from .in_memory_subscribe_database import subscribe_db as db

from ..plans.in_memory_plans_database import plans_db
from ..members.in_memory_members_database import members_db
import uuid

router = APIRouter()

@router.get('/', response_model=List[SubscribeSchema])
async def get_subscribe():
    """Get all subscribe"""
    return list(db.values())

@router.post('/', response_model=SubscribeSchema)
async def create_subscribe(subscribe: SubscribeSchema):
    """Create a new subscribe"""
    subscribe_dict = subscribe.model_dump()
    subscribe_dict['id_subcribe'] = str(uuid.uuid4())
    if subscribe_dict['id_user'] not in members_db:
        raise HTTPException(status_code=404, detail="User not found")
    if subscribe_dict['id_plan'] not in plans_db:
        raise HTTPException(status_code=404, detail="Plan not found")
    db[subscribe_dict['id_subscribe']] = subscribe_dict
    return subscribe_dict

@router.get('/{subscribe_id}', response_model=SubscribeSchema)
async def show_subscribe(subscribe_id: str):
    """Show a plan by id"""

    if subscribe_id not in db:
        raise HTTPException(status_code=404, detail="Plan not found")

    return db[subscribe_id]

@router.put('/{subscribe_id}', response_model=SubscribeSchema)
async def update_subscribe(subscribe_id: str, subscribe: SubscribeSchema):
    """Update a subscribe by id"""

    if subscribe_id not in db:
        raise HTTPException(status_code=404, detail="Plan not found")

    subscribe_dict = subscribe.model_dump()
    subscribe_dict['id_subscribe'] = subscribe_id
    db[subscribe_id] = subscribe_dict
    return subscribe_dict

@router.delete('/{subscribe_id}', response_model=SubscribeSchema)
async def delete_subscribe(subscribe_id: str):
    """Delete a subscribe by id"""

    if subscribe_id not in db:
        raise HTTPException(status_code=404, detail="Plan not found")

    return db.pop(subscribe_id)