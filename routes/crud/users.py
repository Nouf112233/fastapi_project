from sqlalchemy.orm import session
# from models import users as musers
from schemas.users import Users as sUsers
from database import get_db
from passlib.context import CryptContext
from fastapi import status, HTTPException
from sqlalchemy.orm import session
import models.users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user:sUsers ,db:session):
    hashed_pass = pwd_context.hash(user.password)
    
    new_user = models.users.Users(
        email=user.email,
        password=hashed_pass,
        username=user.username,
       
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
  
# def get(id: int):
#     user = main.db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with id {id} is not Available")
#     return user