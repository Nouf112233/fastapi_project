from sqlalchemy.orm import session
from fastapi import APIRouter, status, HTTPException, Response, Depends
from routes.crud import roles as cRoles
from schemas import roles 
from database import get_db

router = APIRouter(tags=["roles"], prefix="/roles")

@router.post('/')
def newRole(rolee: roles.Roles, db:session = Depends(get_db)):
    return cRoles.create_role(rolee,db)