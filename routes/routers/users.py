from fastapi import APIRouter, status, HTTPException, Response, Depends
# from typing import Optional,List
# from crud import users
from oauth2 import get_current_user
from sqlalchemy.orm import session
from database import get_db
from routes.crud import users as cUsers
from schemas import users as sUsers
# from routes.crud import roles as cRoles
# from schemas import roles

router = APIRouter(tags=["users"], prefix="/users")

@router.post('/')
def createUser(user: sUsers.Users,db:session=Depends(get_db)):
    return cUsers.create_user(user,db)