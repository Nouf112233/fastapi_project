
from sqlalchemy.orm import session
from models import posts as m_posts
from schemas import posts as s_posts
from schemas import users as s_users
from fastapi import status, HTTPException

def create_post(post: s_posts.Posts,db:session,current_user:int):
    new_post = m_posts.Posts(
       disc=post.disc,
       image=post.image,
       time=post.time,
       user_id=current_user
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db:session):
   posts=db.query(m_posts.Posts).all()
   return posts

def get_post(post_id:int,db:session):
   post=db.query(m_posts.Posts).get(post_id)
   return post

def update_post(post_id:int,disc:str,image:str,db:session,current_user:int):
   oldPost=db.query(m_posts.Posts).filter(m_posts.Posts.id==post_id).first()
   if oldPost.user_id==current_user:
      if disc:
         db.query(m_posts.Posts).filter(m_posts.Posts.id==post_id).update({m_posts.Posts.disc:disc})
         db.commit()
      if image:
         db.query(m_posts.Posts).filter(m_posts.Posts.id==post_id).update({m_posts.Posts.image:image})
         db.commit()

      return {"msg":"update post done secssusfully"}
   else:
      return {"msg":"The user does not have permission to edit"}

def delete_post(id:int,db:session,current_user:int):
   post = db.query(m_posts.Posts).filter(m_posts.Posts.id == id).first()
   if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user Not Found")
   if post.user_id==current_user:
       db.delete(post)
       db.commit()
       return {"msg":"delete post done sucssefuly"}
   return {"msg":"The user does not have permission to delete"}





   