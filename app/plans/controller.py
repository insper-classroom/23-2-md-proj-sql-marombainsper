from typing import List

from fastapi import APIRouter, HTTPException
from .schema import PlansSchema
from app.base import CamelModel
from .in_memory_plans_database import plans_db as db
from ..members.in_memory_members_database import members_db
from ..subscriptions.in_memory_subscribe_database import subscribe_db
from ..members.schema import UserSchema
import uuid

router = APIRouter()

class PlanMembersSchema(CamelModel):
    members: List[UserSchema] = []
    plan: PlansSchema


@router.get('/', response_model=List[PlansSchema])
async def get_plans():
    """Get all Plans"""
    return list(db.values())

@router.get('/{plan_id}/members', response_model=PlanMembersSchema)
async def get_members_of_plan(plan_id: str):
    """Get all members of a plan"""

    if plan_id not in db:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    members_ids = [subscribe['id_user'] for subscribe in subscribe_db.values() if subscribe['id_plan'] == plan_id]
    return {
        'members': [members_db[member_id] for member_id in members_ids],
        'plan': db[plan_id]
    }

@router.post('/', response_model=PlansSchema)
async def create_plan(plan: PlansSchema):
    """Create a new plan"""
    plan_dict = plan.model_dump()
    plan_dict['id'] = str(uuid.uuid4())
    db[plan_dict['id']] = plan_dict
    return plan_dict

@router.get('/{plan_id}', response_model=PlansSchema)
async def show_plan(plan_id: str):
    """Show a plan by id"""

    if plan_id not in db:
        raise HTTPException(status_code=404, detail="Plan not found")

    return db[plan_id]

@router.put('/{plan_id}', response_model=PlansSchema)
async def update_plan(plan_id: str, plan: PlansSchema):
    """Update a plan by id"""

    if plan_id not in db:
        raise HTTPException(status_code=404, detail="Plan not found")

    plan_dict = plan.model_dump()
    plan_dict['id'] = plan_id
    db[plan_id] = plan_dict
    return plan_dict

@router.delete('/{plan_id}', response_model=PlansSchema)
async def delete_plan(plan_id: str):
    """Delete a plan by id"""

    if plan_id not in db:
        raise HTTPException(status_code=404, detail="Plan not found")

    return db.pop(plan_id)