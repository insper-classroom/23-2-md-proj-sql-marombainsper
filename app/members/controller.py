from typing import List

from fastapi import APIRouter, HTTPException, Depends
from .schema import MemberSchema
from .service import UserService
from app.db import get_db, Session
import uuid

router = APIRouter()

@router.get('/', response_model=List[MemberSchema])
async def get_members(session: Session = Depends(get_db)):
    """Get all Members"""
    return await UserService.get_all(session)

@router.post('/', response_model=MemberSchema)
async def create_member(member: MemberSchema, session: Session = Depends(get_db)):
    """Create a new member"""
    return await UserService.create(member, session)

@router.get('/{member_id}', response_model=MemberSchema)
async def show_member(member_id: str, session: Session = Depends(get_db)):
    """Show a member by id"""

    resp = await UserService.show_member(member_id, session)
    if resp:
        return resp
    else:
        raise HTTPException(status_code=404, detail="Member not found")

@router.put('/{member_id}', response_model=MemberSchema)
async def update_member(member_id: str, member: MemberSchema, session: Session = Depends(get_db)):
    """Update a member by id"""

    resp = await UserService.update_member(member_id, member, session)
    if resp:
        return resp
    else:
        raise HTTPException(status_code=404, detail="Member not found")

@router.delete('/{member_id}', response_model=MemberSchema)
async def delete_member(member_id: str, session: Session = Depends(get_db)):
    """Delete a member by id"""

    resp = await UserService.delete_member(member_id, session)
    if resp:
        return resp
    else:
        raise HTTPException(status_code=404, detail="Member not found")
