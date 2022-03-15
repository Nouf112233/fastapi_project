from typing import List
from sqlalchemy.orm import session
from fastapi import APIRouter, status, HTTPException, Response, Depends
from routes.crud import posts as cPosts
from schemas import posts,users 
from database import get_db
import oauth2
router = APIRouter(tags=["posts"], prefix="/posts")

# ,current_user:users.Users = Depends(oauth2.get_current_user)
@router.post('/')
def newPost(post: posts.Posts, db:session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    return cPosts.create_post(post,db,current_user)

@router.get('/all',response_model=List[posts.ShowPosts])
def getAllPosts( db:session = Depends(get_db)):
    return cPosts.get_all_posts(db)

@router.get('/',response_model=posts.ShowPost)
def getPost(post_id:int, db:session = Depends(get_db)):
    return cPosts.get_post(post_id,db)

@router.patch('/')
def updatePost(post_id:int, disc:str,image:str,db:session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    return cPosts.update_post(post_id,disc,image,db,current_user)

@router.delete("/")
def deletePost(id:int,db:session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    return cPosts.delete_post(id,db,current_user)