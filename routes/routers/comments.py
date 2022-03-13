from fastapi import APIRouter, status, HTTPException, Response, Depends
from database import get_db
from sqlalchemy.orm import session
from models import comments as m_comments
from schemas import comments as s_comments
from typing import Optional,List
from routes.crud import comments as c_comments
from schemas import posts,users
import oauth2
router = APIRouter(tags=["comments"], prefix="/comments")

@router.post('/')
def newComment(post_id:int,comment: s_comments.Comments ,current_user:users.Users = Depends(oauth2.get_current_user), db:session = Depends(get_db)):
    return c_comments.create_comment(post_id,comment,current_user,db)