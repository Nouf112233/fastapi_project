from sqlalchemy.orm import session
from models.users import Users as mUsers
from schemas.users import Users as sUsers
from database import get_db
from passlib.context import CryptContext
from fastapi import status, HTTPException
from sqlalchemy.orm import session
import hashing
import JWToken
from fastapi.security import OAuth2PasswordRequestForm

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(user:sUsers ,db:session):
    hashed_pass = pwd_context.hash(user.password)
    
    new_user = mUsers(
        email=user.email,
        password=hashed_pass,
        username=user.username,
       )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login(request:OAuth2PasswordRequestForm,db:session):
    user = db.query(mUsers).filter(mUsers.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect Password")

    access_token = JWToken.create_access_token(data={"email": user.email,"id":user.id})
    return {"access_token": access_token, "token_type": "bearer"}
  
def get_user(user_id: int,db:session):
    user = db.query(mUsers).filter(mUsers.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} is not Available")
    return user

def update_user(username:str,db:session,current_user:int):
    db.query(mUsers).filter(mUsers.id == current_user).update({mUsers.username:username})
    db.commit()
    return {"msg":"update username done sucssefuly"}

    
def update_pass(password:str,db:session,current_user:int):
    hashPass=pwd_context.hash(password)
    db.query(mUsers).filter(mUsers.id == current_user).update({mUsers.password:hashPass})
    db.commit()
    return {"msg":"update password done sucssefuly"}

def delete_user(db:session,current_user:int):
    user = db.query(mUsers).filter(mUsers.id == current_user).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user Not Found")

    db.delete(user)
    db.commit()
    return {"msg":"delete user done sucssefuly"}

