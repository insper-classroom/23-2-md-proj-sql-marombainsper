from typing import List

from fastapi import APIRouter, HTTPException, Depends
from .schema import PlansSchema
from app.base import CamelModel
from ..members.schema import MemberSchema
from .service import PlansService
from app.db import get_db, Session
import uuid

router = APIRouter()

class PlanMembersSchema(CamelModel):
    members: List[MemberSchema] = []
    plan: PlansSchema


@router.get('/', response_model=List[PlansSchema])
async def get_plans(session: Session = Depends(get_db)):
    """Get all Plans"""
    return await PlansService.get_all(session)

@router.get('/{plan_id}/members', response_model=PlanMembersSchema)
async def get_members_of_plan(plan_id: str, session: Session = Depends(get_db)):
    """Get all members of a plan"""

    plan = await PlansService.show_plan(plan_id, session)
    if plan:
        members = await PlansService.get_members_of_plan(plan_id, session)
        return PlanMembersSchema(members=members, plan=plan)
    else:
        raise HTTPException(status_code=404, detail="Plan not found")

@router.post('/', response_model=PlansSchema)
async def create_plan(plan: PlansSchema, session: Session = Depends(get_db)):
    """Create a new plan"""
    return await PlansService.create(plan, session)

@router.get('/{plan_id}', response_model=PlansSchema)
async def show_plan(plan_id: str, session: Session = Depends(get_db)):
    """Show a plan by id"""

    resp = await PlansService.show_plan(plan_id, session)
    if resp:
        return resp
    else:
        raise HTTPException(status_code=404, detail="Plan not found")

@router.put('/{plan_id}', response_model=PlansSchema)
async def update_plan(plan_id: str, plan: PlansSchema, session: Session = Depends(get_db)):
    """Update a plan by id"""

    resp = await PlansService.update_plan(plan_id, plan, session)
    if resp:
        return resp
    else:
        raise HTTPException(status_code=404, detail="Plan not found")

@router.delete('/{plan_id}', response_model=PlansSchema)
async def delete_plan(plan_id: str, session: Session = Depends(get_db)
):
    """Delete a plan by id"""

    resp = await PlansService.delete_plan(plan_id, session)
    if resp:
        return resp
    else:
        raise HTTPException(status_code=404, detail="Plan not found")