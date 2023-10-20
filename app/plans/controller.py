from typing import List

from fastapi import APIRouter, HTTPException
from .schema import PlansSchema
from .in_memory_plans_database import plans_db as db
import uuid

router = APIRouter()

@router.get('/', response_model=List[PlansSchema])
async def get_plans():
    """Get all Plans"""
    return list(db.values())

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