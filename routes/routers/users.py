from ast import Dict
from urllib import response
from fastapi import APIRouter, status, HTTPException, Response, Depends
# from typing import Optional,List
# from crud import users
from oauth2 import get_current_user
from sqlalchemy.orm import session
from database import get_db
from routes.crud import users as cUsers
from schemas import users as sUsers
from fastapi.security import OAuth2PasswordRequestForm
import oauth2
# from routes.crud import roles as cRoles
# from schemas import roles

router = APIRouter(tags=["users"], prefix="/users")

@router.post('/')
def createUser(user: sUsers.Users,db:session=Depends(get_db)):
    return cUsers.create_user(user,db)

@router.post('/login')
def log_in(request:OAuth2PasswordRequestForm = Depends(),db:session=Depends(get_db)):
    return cUsers.login(request,db)

@router.get('/',response_model=sUsers.ShowUser)
def getUser(user_id: int,db:session=Depends(get_db)):
    return cUsers.get_user(user_id,db)

@router.put('/')
def updateUser(username:str,db:session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    return cUsers.update_user(username,db,current_user)

@router.put('/')    
def updatePass(password:str,db:session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    return cUsers.update_pass(password,db,current_user)

@router.delete('/')
def deleteUser(db:session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    return cUsers.delete_user(db,current_user)
