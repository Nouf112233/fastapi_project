from sqlalchemy.orm import session
from models import likes as m_likes
from schemas import likes as s_likes
from models import posts as m_posts
from schemas import posts as s_posts
from schemas import users as s_users

def create_like(post_id:int,current_user:int,db:session):
   like=db.query(m_likes.Likes).filter(m_likes.Likes.user_id==current_user and m_likes.Likes.post_id==post_id).first()
   if like is None:
       new_like = m_likes.Likes(
          like=True,
          user_id=current_user,
          post_id=post_id
       )
       db.add(new_like)
       db.commit()
       db.refresh(new_like)
       return new_like
   new=not like.like
   db.query(m_likes.Likes).filter(m_likes.Likes.user_id==current_user and m_likes.Likes.post_id==post_id).update({m_likes.Likes.like:new})
   db.commit()
   return new