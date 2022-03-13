from fastapi import APIRouter, status, HTTPException, Response, Depends
from database import get_db
from sqlalchemy.orm import session
from schemas import posts,users 
from routes.crud import likes as cLikes


import oauth2
router = APIRouter(tags=["likes"], prefix="/likes")

@router.post('/')
def newLike(post_id:int,current_user:users.Users = Depends(oauth2.get_current_user), db:session = Depends(get_db)):
    return cLikes.create_like(post_id,current_user,db)