from sqlalchemy.orm import session
from fastapi import APIRouter, status, HTTPException, Response, Depends
from routes.crud import posts as cPosts
from schemas import posts,users 
from database import get_db
import oauth2
router = APIRouter(tags=["posts"], prefix="/posts")

@router.post('/')
def newPost(post: posts.Posts, db:session = Depends(get_db),current_user:users.Users = Depends(oauth2.get_current_user)):
    return cPosts.create_post(post,current_user,db)