from typing import List

from fastapi import APIRouter, HTTPException
from .schema import UserSchema
from .in_memory_members_database import members_db as db
import uuid

router = APIRouter()

@router.get('/', response_model=List[UserSchema])
async def get_members():
    """Get all Members"""
    return list(db.values())

@router.post('/', response_model=UserSchema)
async def create_member(member: UserSchema):
    """Create a new member"""
    member_dict = member.model_dump()
    member_dict['id'] = str(uuid.uuid4())
    db[member_dict['id']] = member_dict
    return member_dict

@router.get('/{member_id}', response_model=UserSchema)
async def show_member(member_id: str):
    """Show a member by id"""

    if member_id not in db:
        raise HTTPException(status_code=404, detail="Member not found")

    return db[member_id]

@router.put('/{member_id}', response_model=UserSchema)
async def update_member(member_id: str, member: UserSchema):
    """Update a member by id"""

    if member_id not in db:
        raise HTTPException(status_code=404, detail="Member not found")

    member_dict = member.model_dump()
    member_dict['id'] = member_id
    db[member_id] = member_dict
    return member_dict

@router.delete('/{member_id}', response_model=UserSchema)
async def delete_member(member_id: str):
    """Delete a member by id"""

    if member_id not in db:
        raise HTTPException(status_code=404, detail="Member not found")

    return db.pop(member_id)
