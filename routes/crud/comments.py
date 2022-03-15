
from sqlalchemy.orm import session
from models import comments as m_comments
from schemas import comments as s_comments
from models import likes as m_likes
from schemas import likes as s_likes
from models import posts as m_posts
from schemas import posts as s_posts
from schemas import users as s_users
from fastapi import status, HTTPException

def create_comment(post_id:int,comment:s_comments.Comments,db:session,current_user:int):
    new_comment = m_comments.Comments(
       disc=comment.disc,
       time=comment.time,
       user_id = current_user,
       post_id=post_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def delete_comment(id:int,db:session,current_user:int):
   comment = db.query(m_comments.Comments).filter(m_comments.Comments.id == id).first()
   if comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="comment Not Found")
   if comment.user_id==current_user:
       db.delete(comment)
       db.commit()
       return {"msg":"delete comment done sucssefuly"}
   return {"msg":"The user does not have permission to delete"}
