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
def newComment(post_id:int,comment: s_comments.Comments , db:session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    return c_comments.create_comment(post_id,comment,db,current_user)

@router.delete("/")
def deleteComment(id:int,db:session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    return c_comments.delete_comment(id,db,current_user)